''' simple des '''
''' reference https://www.cs.uri.edu/cryptography/dessimplified.htm '''
def calculate_new_r(l, r, key_new, s1_box, s2_box):
	expanded_r = [0 for i in xrange(8)]
	r_new = [0 for i in xrange(6)]
	
	# expand r from 6 to 8 bits	
	expanded_r[0], expanded_r[1], expanded_r[2], expanded_r[3] = r[1], r[0], r[3], r[2]
	expanded_r[4], expanded_r[5], expanded_r[6], expanded_r[7] = r[3], r[2], r[4], r[5]

	# calculate temporary r by XORing with key
	temp_r_new = [0 for x in xrange(8)]
	for index in xrange(len(expanded_r)):
		temp_r_new[index] = key_new[index]^expanded_r[index] # r_i = l_i-1 XOR expanded_r

	# now get values from s1_box and s2_box
	s1 = temp_r_new[0:4]
	temp1 = s1[0]
	temp2 = s1[1]*4 + s1[2]*2 +s1[3]*1
	if temp1 == 0:
		val = s1_box[0][temp2]
		r_new[0:3] = val
	
	s2 = temp_r_new[4:8]
	temp1 = s2[0]
	temp2 = s2[1]*4 + s2[2]*2 +s2[3]*1
	if temp1 == 0:
		val = s2_box[0][temp2]
		r_new[3:6] = val

	return r_new

def new_key(key, index1):
	new_key = [0 for i in xrange(8)]
	return new_key

def simple_des(data_block, key, num_fiestel_cycles, s1_box, s2_box):
	l = data_block[0:6]
	r = data_block[6:12]
	l_new = r
	r_new = [0 for i in xrange(6)]
	new_data_block = [0 for i in xrange(12)]
	

	# apply defined fiestel cycles
	for index1 in xrange(num_fiestel_cycles):
		
		# get key_new by shifting
		key = new_key(key, index1)

		# get new r and l
		l_new = r
		temp = calculate_new_r(l, r, key_new, s1_box, s2_box)
		for index2 in xrange(len(r_new)):
			r_new[index2] = temp[index2] ^ l[index2]
		
		# print("round:{0}\tnew key{1}\t".format(index1,key_new))
		# print("l{0}:{1}\tr{0}:{2}\n".format(index1, l_new, r_new))
		l = l_new
		r = r_new

	new_data_block[0:6] = r_new
	new_data_block[6:12] = l_new

	return new_data_block

def main():
	key = [1, 1, 1, 0, 0, 0, 1, 1, 1] # 9 bit key
	plain_text = [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1] # 12 bit plain text block
	num_fiestel_cycles = 5
	s1_box = [
				[ [1,0,1], [0,1,0], [0,0,1], [1,1,0], [0,1,1], [1,0,0], [1,1,1], [0,0,0] ],
				[ [0,0,1], [1,0,0], [1,1,0], [0,1,0], [0,0,0], [1,1,1], [1,0,1], [0,1,1] ],
			]
	s2_box = [
				[ [1,0,0], [0,0,0], [1,1,0], [1,0,1], [1,1,1], [0,0,1], [0,1,1], [0,1,0] ],
				[ [1,0,1], [0,1,1], [0,0,0], [1,1,1], [1,1,0], [0,1,0], [0,0,1], [1,0,0] ],
			]
	cipher_block = simple_des(plain_text, key, num_fiestel_cycles, s1_box, s2_box)
	decipher_block = simple_des(cipher_block, key, num_fiestel_cycles, s1_box, s2_box)

	print("PLAIN TEXT\t{}".format(plain_text))
	print("CIPHER BLOCK\t{}".format(cipher_block))
	print("DECIPHER BLOCK\t{}".format(decipher_block))

if __name__ == '__main__':
	main()