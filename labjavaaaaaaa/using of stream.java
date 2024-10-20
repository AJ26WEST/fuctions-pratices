import java.util.*;
import java.util.stream.*;

public class StreamExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Using Stream to filter even numbers, multiply them by 2, and collect the result
        List<Integer> evenNumbers = numbers.stream()
                                           .filter(n -> n % 2 == 0)
                                           .map(n -> n * 2)
                                           .collect(Collectors.toList());

        System.out.println(evenNumbers); 
    }
}
