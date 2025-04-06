package Medium.java;

/**
 * Leetcode difficulty: Medium
 * A class that provides a method to generate the maximum area that can be formed between two heights from an array of heights.
 */
public class MaxArea {
    /**
     * Solution 1
     * Runtime: Beats 85.37% of all users
     * Memory: Beats 92.58% of all users
     * 
     * Generates maximum area that can be formed between two heights from an array of heights.
     *
     * @param height An array of heights.
     * @return The maximum area.
     */
    public static int maxArea(int[] height) {
        //Initializes the maximumArea and left/right pointer variables.
        //Left and right pointers represent the 2 pointers used to find the largest area.
        int maxArea = 0;
        int leftPointer = 0;
        int rightPointer = height.length - 1;

        //While the pointers haven't crossed each other, the current area that is formed between the heights they point at is calculated.
        //If the area is larger than the maxArea variable, it is set as the new maxArea.
        //The pointer pointed at the smallest heights between the two is moved closer towards the larger pointer.
        //(Logic) If the width is as big as possible between pointer A and B the the calculated area will be the guaranteed largest area
        //for the smallest of the two heights the pointers are pointed at.
        while (leftPointer < rightPointer) {
            if ((rightPointer - leftPointer) * Math.min(height[leftPointer], height[rightPointer]) > maxArea) {
                maxArea = (rightPointer - leftPointer) * Math.min(height[leftPointer], height[rightPointer]);
            }
            if (height[rightPointer] > height[leftPointer]) {
                leftPointer++;
            }
            else {
                rightPointer--;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        int[] heights = new int[]{1,8,6,2,5,4,8,3,7};
        System.out.println(maxArea(heights));
    }
}
