import java.io.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());
        
        // List to store names that match the Gmail criteria
        List<String> gmailUsers = new ArrayList<>();
        
        // RegEx pattern to match email addresses ending in @gmail.com
        // The '.' must be escaped with \\ because . is a wildcard in RegEx
        String emailRegEx = ".+@gmail\\.com$";
        Pattern pattern = Pattern.compile(emailRegEx);

        for (int i = 0; i < N; i++) {
            String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            String firstName = firstMultipleInput[0];
            String emailID = firstMultipleInput[1];
            
            // Check if the email matches the pattern
            Matcher matcher = pattern.matcher(emailID);
            if (matcher.find()) {
                gmailUsers.add(firstName);
            }
        }

        // Sort names alphabetically
        Collections.sort(gmailUsers);

        // Print each name on a new line
        for (String name : gmailUsers) {
            System.out.println(name);
        }

        bufferedReader.close();
    }
}
