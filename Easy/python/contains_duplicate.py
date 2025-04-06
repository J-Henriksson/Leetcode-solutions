class ContainsDuplicate():

    def contains_duplicate(self, nums):
        """Returns True if an array contains duplicates and False if it doesn't. Does this by sorting the list and then comparing each value to the previous value, if they match then the list
        contains a duplicate.

        Analysis: Pretty decent solution to a very simple problem. Time complexity of O(nlog(n)). Time complexity could be reduced by using a hashmap.
        Runtime: Beats 7.65% :(
        Memory: Beats 94.93%

        Args:
            nums (list): List of numbers to be checked for duplicates.

        Returns:
            boolean: True if the list contains duplicates, otherwise false.
        """
        nums.sort()
        for num in range(1, len(nums)):
            if nums[num] == nums[num - 1]:
                return True
        return False
    
if __name__ == "__main__":
    contains_duplicate = ContainsDuplicate()
    nums = [1,4,5,6,2,7]

    print(contains_duplicate.contains_duplicate(nums))