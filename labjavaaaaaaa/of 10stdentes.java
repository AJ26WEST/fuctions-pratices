import java.util.Scanner;

class Student {
    String name;
    int rollNo;
    double percentage;

    // Constructor to initialize student details
    public Student(String name, int rollNo, double percentage) {
        this.name = name;
        this.rollNo = rollNo;
        this.percentage = percentage;
    }

    // Method to display student details
    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
        System.out.println("Percentage: " + percentage + "%");
        System.out.println();
    }
}

public class StudentDetails {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Student[] students = new Student[10];

        // Collecting student details
        for (int i = 0; i < 10; i++) {
            System.out.println("Enter details for student " + (i + 1) + ":");
            System.out.print("Name: ");
            String name = scanner.nextLine();
            System.out.print("Roll No: ");
            int rollNo = scanner.nextInt();
            System.out.print("Percentage: ");
            double percentage = scanner.nextDouble();
            scanner.nextLine(); // Consume newline

            students[i] = new Student(name, rollNo, percentage);
            System.out.println();
        }

        // Displaying student details using a traditional for loop
        System.out.println("Student Details:");
        for (int i = 0; i < students.length; i++) {
            students[i].display();
        }

        scanner.close();
    }
}
