import java.util.Scanner;

class Employee {
    private String name;
    private int age;
    private String phone;
    private String address;
    private double salary;

    public Employee(String name, int age, String phone, String address, double salary) {
        this.name = name;
        this.age = age;
        this.phone = phone;
        this.address = address;
        this.salary = salary;
    }

    public void displayEmployee() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Phone Number: " + phone);
        System.out.println("Address: " + address);
        System.out.println("Salary: $" + salary);
    }
}

class Manager extends Employee {
    private String specialization;
    private String department;

    public Manager(String name, int age, String phone, String address, double salary, String specialization, String department) {
        super(name, age, phone, address, salary);
        this.specialization = specialization;
        this.department = department;
    }

    public void displayManager() {
        System.out.println("\n=== Manager Details ===");
        displayEmployee();
        System.out.println("Specialization: " + specialization);
        System.out.println("Department: " + department);
        System.out.println("=======================\n");
    }
}

class Officer extends Employee {
    private String specialization;
    private String department;

    public Officer(String name, int age, String phone, String address, double salary, String specialization, String department) {
        super(name, age, phone, address, salary);
        this.specialization = specialization;
        this.department = department;
    }

    public void displayOfficer() {
        System.out.println("\n=== Officer Details ===");
        displayEmployee();
        System.out.println("Specialization: " + specialization);
        System.out.println("Department: " + department);
        System.out.println("=======================\n");
    }
}

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Manager details input
        System.out.println("Enter Manager Details");
        System.out.print("Name: ");
        String managerName = sc.nextLine();
        System.out.print("Age: ");
        int managerAge = sc.nextInt();
        sc.nextLine();  // Consume newline
        System.out.print("Phone Number: ");
        String managerPhone = sc.nextLine();
        System.out.print("Address: ");
        String managerAddress = sc.nextLine();
        System.out.print("Salary: ");
        double managerSalary = sc.nextDouble();
        sc.nextLine();  // Consume newline
        System.out.print("Specialization: ");
        String managerSpecialization = sc.nextLine();
        System.out.print("Department: ");
        String managerDepartment = sc.nextLine();

        Manager manager = new Manager(managerName, managerAge, managerPhone, managerAddress, managerSalary, managerSpecialization, managerDepartment);
        manager.displayManager();

        // Officer details input
        System.out.println("Enter Officer Details");
        System.out.print("Name: ");
        String officerName = sc.nextLine();
        System.out.print("Age: ");
        int officerAge = sc.nextInt();
        sc.nextLine();  // Consume newline
        System.out.print("Phone Number: ");
        String officerPhone = sc.nextLine();
        System.out.print("Address: ");
        String officerAddress = sc.nextLine();
        System.out.print("Salary: ");
        double officerSalary = sc.nextDouble();
        sc.nextLine();  // Consume newline
        System.out.print("Specialization: ");
        String officerSpecialization = sc.nextLine();
        System.out.print("Department: ");
        String officerDepartment = sc.nextLine();

        Officer officer = new Officer(officerName, officerAge, officerPhone, officerAddress, officerSalary, officerSpecialization, officerDepartment);
        officer.displayOfficer();

        sc.close();
    }
}
