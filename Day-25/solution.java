import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // Number of test cases

        while (T-- > 0) {
            int n = sc.nextInt();
            if (isPrime(n)) {
                System.out.println("Prime");
            } else {
                System.out.println("Not prime");
            }
        }
        sc.close();
    }

    public static boolean isPrime(int n) {
        // 1 is not prime, 2 is prime
        if (n < 2) return false;
        if (n == 2) return true;
        
        // Eliminate even numbers early
        if (n % 2 == 0) return false;

        // Check odd divisors from 3 up to sqrt(n)
        // Complexity: O(sqrt(n))
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
