class RemoveDuplicates():

    def remove_duplicates(self, nums):
        """Goes through a list of ints sorted in increasing order and moves all duplicates to the end of the list. Does this by looping through the list and
        storing the index for the most recent unique number in a variable and comparing each new value to the number at that index. 
        If the new value doesn't match then the index is increased by 1 and the new number is added as the value for that index. 

        Analysis: Very basic problem with a very basic solution. Time complexity of O(n).
        Runtime: Beats 100%
        Memory: Beats 36.16%

        Args:
            nums (list): List of numbers sorted in increasing order.

        Returns:
            int: The amount of unique numbers in the list.
        """
        index = 0
        for num in range(1, len(nums)):
            if nums[num] != nums[index]:
                index +=1
                nums[index] = nums[num]
        return index + 1
    
if __name__ == "__main__":
    nums = [1,1,2]
    remove_duplicates = RemoveDuplicates()
    
    print(remove_duplicates.remove_duplicates(nums))
    print(nums)