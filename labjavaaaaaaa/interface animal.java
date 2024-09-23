// Base class ANIMAL
class Animal {
    public int legs; // Public allows access from anywhere

    public Animal(int legs) {
        this.legs = legs;
    }

    public void eat() {
        System.out.print("\nThis animal eats.");
    }

    public void walk() {
        System.out.print("\nThis animal walks by " + legs + " legs");
    }
}

// Interface PET
interface Pet {
    String getName();
    void setName(String name);
}

// Class SPIDER
class Spider extends Animal {
    public Spider() {
        super(8); // Spiders have 8 legs
    }

    @Override
    public void eat() {
        System.out.print("\nSpider eats insects");
    }
}

// Class CAT
class Cat extends Animal implements Pet {
    public String name; // Public name variable

    public Cat(String name) {
        super(4); // Cats have 4 legs
        this.name = name;
    }

    @Override
    public void eat() {
        System.out.print("\nCat eats fish");
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void setName(String name) {
        if (name != null && !name.trim().isEmpty()) {
            this.name = name;
        } else {
            System.out.print("\nInvalid name provided.");
        }
    }
}

// Class FISH
class Fish extends Animal implements Pet {
    public String name; // Public name variable

    public Fish(String name) {
        super(0); // Fish have no legs
        this.name = name;
    }

    @Override
    public void eat() {
        System.out.print("\nFish eats plants");
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void setName(String name) {
        if (name != null && !name.trim().isEmpty()) {
            this.name = name;
        } else {
            System.out.print("\nInvalid name provided.");
        }
    }

    @Override
    public void walk() {
        System.out.print("\nFish swims instead of walking");
    }
}

// MAIN class
public class InterfaceInheritance {
    public static void main(String[] args) {
        System.out.print("FISH");
        Fish fish = new Fish("Mimi");
        System.out.print("\nThis fish's name is " + fish.getName());
        fish.eat();
        fish.walk();

        System.out.print("\n\nCAT");
        Cat cat = new Cat("MiMi");
        System.out.print("\nThis cat's name is " + cat.getName());
        cat.walk();
        cat.eat();
        cat.setName("Mouse");
        System.out.print("\nThis cat's name is " + cat.getName());

        System.out.print("\n\nSPIDER");
        Spider spider = new Spider();
        spider.eat();
        spider.walk();
    }
}
