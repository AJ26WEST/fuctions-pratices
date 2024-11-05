*//
interface Animal {
    void eat();
}

// Second interface
interface Bird {
    void fly();
}

// Class that implements both interfaces
class Bat implements Animal, Bird {
    // Implementing method from Animal interface
    public void eat() {
        System.out.println("The bat is eating.");
    }

    // Implementing method from Bird interface
    public void fly() {
        System.out.println("The bat is flying.");
    }
}

// Main class to test the implementation
public class MultipleInheritanceExample {
    public static void main(String[] args) {
        Bat bat = new Bat();
        
        // Calling methods from both interfaces
        bat.eat();
        bat.fly();
    }
}
