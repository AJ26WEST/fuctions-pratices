import java.util.Scanner;

public class PrimeCheck {

    // Method to check if a number is prime
    public static boolean isPrime(int number) {
        // Prime numbers are greater than 1
        if (number <= 1) {
            return false;
        }
        
        // Check for factors from 2 to the square root of the number
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;  // If divisible by any number, it's not prime
            }
        }
        return true;  // If no divisors found, it's prime
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input from the user
        System.out.println("Enter a number: ");
        int userInput = sc.nextInt();

        // Check if the number is prime
        if (isPrime(userInput)) {
            System.out.println(userInput + " is a prime number.");
        } else {
            System.out.println(userInput + " is not a prime number.");
        }

        sc.close();
    }
}
