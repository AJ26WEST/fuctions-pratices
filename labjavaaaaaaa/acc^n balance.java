public class Account {
  private double balance = 500.00;  // member data
  public double  getBalance(int AccNum) {     // member method
    // logic here
    return balance;
  }
  public static void main(String[] args) {
    Account accnt = new Account();            // object creation
    double value = accnt.getBalance(96325);
    System.out.println("The balance is: " + value);
  }
}
