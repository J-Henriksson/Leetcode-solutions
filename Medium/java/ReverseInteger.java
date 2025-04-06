package Medium;

/**
 * Leetcode difficulty: Medium
 * A class that provides a method to generate the reverse of a given int.
 */
public class ReverseInteger {
    /**
     * Solution 1
     * Runtime: Beats 97.62% of all users
     * Memory: Beats 85.95% of all users
     * 
     * Generates the reverse of an int and returns 0 if the reverse is out of javas 32 bit bounds.
     *
     * @param x An int to be reversed.
     * @return The reversed int or 0 if the reverse is out of bounds.
     */
    public static int reverse(int x) {
        //Initializes two variables. NumberBeforeReversed is used to extract each digit in reversed order. Reversed is used to store the new reversed number.
        int numberBeforeReversed = x;
        int reversed = 0;

        //While numberBeforeReversed does not equal zero which it will when all the numbers have been extracted, the loop continues.
        while (numberBeforeReversed != 0) {
            //If the reversed number will cause a overflow or underflow once it is multiplied by 10 to add the next number, 0 is returned.
            if (reversed < Integer.MIN_VALUE / 10 || reversed > Integer.MAX_VALUE / 10) {
                return 0;
            }
            //Multiply the current value of reversed by 10 and add the last digit of numberBeforeReversed.
            //Then divide numberBeforeReversed by 10 to remove the  last digit.
            reversed = (reversed * 10) + numberBeforeReversed % 10;
            numberBeforeReversed /= 10;
        }

        //When the while loop has finished return reversed.
        return reversed;
    }

    public static void main(String[] args) {
        System.out.println(reverse(153423699));
    }
}
