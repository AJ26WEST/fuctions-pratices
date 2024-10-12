class Main {

    public static void main(String[] args) {
        Student abhi = new Student();
        var v = .2f;
        abhi.setDetails(21, "abhishek",67.9f);
        abhi.displayDetails();
    }
}

class Student {
    int rnoll;
    String name;
    Float marks ;

    // Method to set details using 'this' keyword
    void setDetails(int rnoll, String name,Float marks) {
        this.rnoll = rnoll; // 'this' refers to the current object instance
        this.name = name;
        this.marks = marks ;
    }

    // Method to display details
    void displayDetails() {
        System.out.println(this.rnoll); // Optional use of 'this'
        System.out.println(this.name);
        System.out.println(this.marks);// Optional use of 'this'
    }
}

