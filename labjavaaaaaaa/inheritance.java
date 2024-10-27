// Base class (Parent class)
class Vehicle {
    void start() {
        System.out.println("The vehicle starts.");
    }
    
    void stop() {
        System.out.println("The vehicle stops.");
    }
}

// Derived class (Child class)
class Car extends Vehicle {
    void honk() {
        System.out.println("The car honks.");
    }
}

// Another derived class
class Motorcycle extends Vehicle {
    void revEngine() {
        System.out.println("The motorcycle revs its engine.");
    }
}

// Main class to test the inheritance
public class InheritanceExample {
    public static void main(String[] args) {
        Car car = new Car();
        Motorcycle motorcycle = new Motorcycle();

        // Calling methods from the base class
        car.start();          // Output: The vehicle starts.
        car.honk();          // Output: The car honks.
        car.stop();          // Output: The vehicle stops.

        motorcycle.start();   // Output: The vehicle starts.
        motorcycle.revEngine(); // Output: The motorcycle revs its engine.
        motorcycle.stop();     // Output: The vehicle stops.
    }
}
