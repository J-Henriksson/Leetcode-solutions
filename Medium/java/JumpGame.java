package Medium.java;

/**
 * Leetcode difficulty: Medium
 * A class that provides a method to determine if it is possible to reach the last index of an array
 * by making jumps based on the values in the array.
 */
public class JumpGame {
    /**
     * Solution 1
     * Runtime: Beats 44.52% of all users
     * Memory: Beats 97.38% of all users
     * 
     * Determines if it is possible to reach the last index of an array by making jumps based on the values in the array.
     *
     * @param nums An array of non-negative integers representing the maximum jump length at each position.
     * @return True if it is possible to reach the last index, otherwise false.
     */
    public static boolean canJump(int[] nums) {
        // Array to store the index of all zeros.
        int[] zeros = new int[nums.length + 1];
        
        //Variable to keep track of what zero we're on while lopping through the nums array.
        int zerosIndex = 0;

        // Cycles through each value of the int array. If the value is zero and isn't the arrays last element its index
        // is  added to the zeros array and zeros index is incremented.
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0 && i != nums.length - 1) {
                zeros[zerosIndex] = i;
                zerosIndex++;
            }
        }

        // If zerosIndex has never been incremented there are no zeros in the nums array and we can return true.
        if (zerosIndex == 0) {
            return true;
        }

        // Uses sentinel values to set the last element of the zeros array to -1.
        // Since the if statements below won't apply once you've passed the last zero.
        // Also sets zerosIndex to zero in order to reuse it.
        zeros[zerosIndex] = -1;
        zerosIndex = 0;

        // Loops through all elements of num and if the current element is enough to pass the closest zero,
        // zerosIndex is incremented. 1 is subtracted from i in order to see if the current element is enough
        // to pass the next element. If no elements before a zero are not big enough to pass it, false is returned.
        // If the entire nums array is looped through without returning false, true is returned.
        for (int i = 0; i < nums.length; i++) {
            if ((nums[i] - zeros[zerosIndex] + i > 0) && zeros[zerosIndex] != -1) {
                zerosIndex++;
                i--;
            }
            if (i >= zeros[zerosIndex] && zeros[zerosIndex] != -1 ) {
                return false;
            }
        }

        return true;
    }


    /**
     * Solution 2
     * Runtime: Beats 81.42% of all users
     * Memory: Beats 47.63% of all users
     * 
     * Determines if it is possible to reach the last index of an array by making jumps based on the values in the array.
     *
     * @param nums An array of non-negative integers representing the maximum jump length at each position.
     * @return True if it is possible to reach the last index, otherwise false.
     */
    public static boolean canJump2(int[] nums) {
        //Sets initial value of reach variable which represents the furthest index of the array that can be reached at any given point.
        int reach = 0;
        
        //Loops through the nums array. If an index is reached which is beyond the reach, false is returned. 
        // The looped through index with the longest reach is set as the reach until a new index surpasses it.
        // If the entire array is looped through without any index surpassing the reach, true is returned.
        for (int i = 0; i < nums.length; i++) {
            if (i > reach) {
                return false;
            }

            if (i + nums[i] > reach) {
                reach = i + nums[i];
            }
        }

        return true;
    }

    public static void main(String[] args) {
        int[] jumpGame = new int[]{1, 3, 2, 2, 0, 2, 0, 5, 0, 0, 0, 0, 0};
        System.out.println(canJump2(jumpGame) + " " + canJump(jumpGame));
    }
}