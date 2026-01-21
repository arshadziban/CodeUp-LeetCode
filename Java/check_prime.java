import java.util.Scanner;

public class check_prime {
    
    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        if (number == 2) {
            return true;
        }
        
        if (number % 2 == 0) {
            return false;
        }
        
        for (int i = 3; i * i <= number; i += 2) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        
        if (scanner.hasNextInt()) {
            int number = scanner.nextInt();
            
            if (isPrime(number)) {
                System.out.println(number + " is a PRIME number.");
            } else {
                System.out.println(number + " is NOT a prime number.");
            }
        } else {
            System.out.println("Invalid input!");
        }

        scanner.close();
    }
}
