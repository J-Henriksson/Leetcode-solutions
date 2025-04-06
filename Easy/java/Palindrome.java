package Easy.java;

/**
 * Leetcode difficulty: Easy
 * A class that provides a method to determine if a given number is a palindrome, i.e, if a number is the same when reversed.
 */
public class Palindrome {

    /**
     * Solution 1
     * Runtime: Beats 8.35% of all users
     * Memory: Beats 6.16% of all users
     * 
     * Determines if a given number is a palindrome by reversing it and converting it into a String.
     *
     * @param x An int to be checked if it is a palindrome or not.
     * @return True if the number is a palindrome.
     */
    public boolean isPalindrome(int x) {
        // Returns the boolean value of a String based comparison of the given number and its reverse.
        return String.valueOf(x).equals(reverse(x));
    }
        
    /**
     * Generates a String of the reverse of the given int.
     *
     * @param x The int to be reversed.
     * @return A String of the reversed int.
     */
    public String reverse(int x) {
        // Converts the int to a String and loops through each char in reverse order placing them in a new String called reversed.
        String xString = String.valueOf(x);
        String reversed = "";
        for (int i = xString.length() - 1; i >= 0; i--) {
            reversed += xString.charAt(i);
        }

        return reversed;
    }


    /**
     * Solution 1 improved
     * Runtime: Beats 9.69% of all users
     * Memory: Beats 6.16% of all users
     * 
     * Determines if a given number is a palindrome by comparing the numbers within it as chars.
     *
     * @param x An int to be checked if it is a palindrome or not.
     * @return True if the number is a palindrome.
     */
    public static boolean isPalindromeImproved(int x) {
        //Loops through half of the ints chars and checks if the first half matches the second half.
        for (int i = 0; i < String.valueOf(x).length() / 2; i++) {
            if (String.valueOf(x).charAt(i) != String.valueOf(x).charAt(String.valueOf(x).length() - 1 - i)) {
                return false;
            }
        }

        return true;
    }


    /**
     * Solution 2
     * Runtime: Beats 73.27% of all users
     * Memory: Beats 88.96% of all users
     * 
     * Determines if a given number is a palindrome by comparing it with it's reverse.
     *
     * @param x An int to be checked if it is a palindrome or not.
     * @return True if the number is a palindrome.
     */
    public static boolean isPalindrome2(int x) {
        // If the number is negative it cannot be a palindrome and will therefore return false.
        if (x < 0) {
            return false;
        }

        //Initializes two variables, getDigits is used to get the reversed digits for the reversed number 
        //and reversed is used to store the reversed digits.
        int getDigits = x;
        int reversed = 0;
        //While getDigits still has digits, whatever number exists in reversed is multiplied by 10 
        //and the last digit of getDigits is added. GetDigits is then divided by 10 as to not contain the digit 
        //that has just been added to reversed.  
        while (getDigits > 0) {
            reversed = (reversed * 10) + getDigits % 10;
            getDigits /= 10;
        }

        //If after the while loop has finished, the new reversed number equals x, true is returned.
        if (reversed == x) {
            return true;
        }
        //If non of the above conditions are met, false is returned.
        return false;
     }
        
    
    

    public static void main(String[] args) {
        System.out.println(isPalindrome2(1911));
    }
}
