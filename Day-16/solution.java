import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        
        try {
            int num = Integer.parseInt(s);
            System.out.println(num);
        } catch (Exception e) {
            System.out.println("Bad String");
        }
    }
}
