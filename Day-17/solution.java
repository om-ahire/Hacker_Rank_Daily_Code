import java.util.*;
import java.io.*;

//Write your code here
class Calculator {
    int power(int n, int p) throws Exception {
        // Check if either n or p is negative
        if (n < 0 || p < 0) {
            // Throw a new exception with the specific message required
            throw new Exception("n and p should be non-negative");
        }
        // Return n raised to the power of p
        return (int) Math.pow(n, p);
    }
}

class Solution{

    public static void main(String[] args) {
    
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while (t-- > 0) {
        
            int n = in.nextInt();
            int p = in.nextInt();
            Calculator myCalculator = new Calculator();
            try {
                int ans = myCalculator.power(n, p);
                System.out.println(ans);
            }
            catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
        in.close();
    }
}
