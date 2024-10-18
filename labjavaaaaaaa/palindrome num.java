import java.util.Scanner;

public class PalindromeCheck {

    // Method to check if a string is a palindrome
    public static boolean isPalindrome(String input) {
        int left = 0;
        int right = input.length() - 1;

        while (left < right) {
            if (input.charAt(left) != input.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input from user
        System.out.println("Enter a number or string: ");
        String userInput = sc.nextLine();

        // Check if the input is palindrome
        if (isPalindrome(userInput)) {
            System.out.println(userInput + " is a palindrome.");
        } else {
            System.out.println(userInput + " is not a palindrome.");
        }

        sc.close();
    }
}
