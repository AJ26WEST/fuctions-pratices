import java.util.Scanner;

public class ArmstrongCheck {

    // Method to check if a number is an Armstrong number
    public static boolean isArmstrong(int number) {
        int originalNumber = number;
        int result = 0;
        int numberOfDigits = String.valueOf(number).length();

        while (number != 0) {
            int digit = number % 10; // Extract the last digit
            result += Math.pow(digit, numberOfDigits); // Add the digit raised to the power of the number of digits
            number /= 10; // Remove the last digit
        }

        // If the sum is equal to the original number, it's an Armstrong number
        return result == originalNumber;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input from the user
        System.out.println("Enter a number: ");
        int userInput = sc.nextInt();

        // Check if the number is Armstrong
        if (isArmstrong(userInput)) {
            System.out.println(userInput + " is an Armstrong number.");
        } else {
            System.out.println(userInput + " is not an Armstrong number.");
        }

        sc.close();
    }
}
