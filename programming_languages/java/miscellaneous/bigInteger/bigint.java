import java.math.BigInteger;
public class bigint
{
  public static void main(String[] args) 
  {
  BigInteger bigInteger1 = new BigInteger ("123456789");
  BigInteger bigInteger2 = new BigInteger ("112334");
  BigInteger bigIntResult = bigInteger1.multiply(bigInteger2);
  System.out.println("Result is  ==> " + bigIntResult);
  }
}