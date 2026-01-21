import java.util.Scanner;

public class reverse_string {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // user input
        System.out.print("Enter a string to reverse: ");
        String input = scanner.nextLine();
        
        String reversed = new StringBuilder(input).reverse().toString();
        

        // display
        System.out.println("Original string: " + input);
        System.out.println("Reversed string: " + reversed);
        
        scanner.close();
    }
}
