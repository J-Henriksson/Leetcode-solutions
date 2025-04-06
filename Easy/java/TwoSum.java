package Easy.java;

import java.util.HashMap;

/**
 * Leetcode difficulty: Easy
 * A class that provides a method that takes an array of ints and a target int, and returns the two ints from the array that added up give the target.
 */
public class TwoSum {
    /**
     * Solution 1
     * Runtime: Beats 81.45% of all users
     * Memory: Beats 36.08% of all users
     * 
     * Determines what numbers within the int add upp to a specific target.
     *
     * @param nums An array to be checked for two numbers that add upp to the target.
     * @param target An int for the numebrs within the array to be checked in regards to.
     * @return An array with the two numbers that add upp to the target.
     */
    public static int[] twoSum(int[] nums, int target) {
        //Creates a new HashMap to store the numbers of the array and index.
        HashMap<Integer, Integer> loopedThroughNumbers = new HashMap<>();
        //Loops through each value of the nums array. 
        //If the value needed to be added to the current value (target - nums[i]) already has been added to the HashMap
        // And array with the index of that value and the current index is returned.
        // If (target - nums[i]) hasn't been added to the HashMap the current value and it's index are added. 
        for (int i = 0; i < nums.length; i++) {
            if (loopedThroughNumbers.containsKey(target - nums[i])) {
                return new int[]{loopedThroughNumbers.get(target - nums[i]), i};
            }
            else {
                loopedThroughNumbers.put(nums[i], i);
            }
        }

        //If two numbers that add upp to the target can't be found within the array, an empty array is returned.
        return new int[]{};
        
    }

    public static void main(String[] args) {
         int[] numbers = {1, 2, 4, 5};
        System.out.println(twoSum(numbers, 6)[0] + " " + twoSum(numbers, 6)[1]);
    }
}
