class MaximumCount():
    def maximum_count_v1(self, nums):
        """Finds the amount of positive integers and the amount of negative integers and returns whichever amount is the largest.

        Analysis: Kind of a brute force solution but overall pretty good.
        Runtime: Beats 60.94%
        Memory: Beats 58.15%

        Args:
            nums (list): Sorted list of numbers.

        Returns:
            int: The amount of positive of negative numbers.
        """
        if nums[0] * nums[len(nums) - 1] > 0:
            return len(nums)
        if nums[0] == 0 and nums[len(nums) - 1] == 0:
            return 0
        
        count = 0
        for x in range(len(nums)):
            if nums[x] < 0:
                count += 1
            if nums[x] > 0:
                break
        if len(nums) - x > count:
            return len(nums) - x
        return count
    

    def maximum_count_v2(self, nums):
        """Cool solution using a unique implementation of binary search.

        Analysis: Very effective solution although it is a bit overly complicated.
        Runtime: Beats 100%
        Memory: Beats 90.35%

        Args:
            nums (list): Sorted list of numbers.

        Returns:
            index (int): The amount of positive of negative numbers.
        """
        neg_end = self.binary_search_closest_number(nums, 0)
        pos_end = self.binary_search_closest_number(nums, 1)
        if neg_end > len(nums) - pos_end:
            return neg_end
        return len(nums) - pos_end

    def binary_search_closest_number(self, nums, target):
        top = len(nums) - 1
        bottom = 0
        index = len(nums)
        while top >= bottom:
            mid = (top + bottom) // 2

            if nums[mid] < target:
                bottom = mid + 1
            else:
                top = mid - 1
                index = mid
        return index
    
if __name__ == "__main__":
    maximum_count = MaximumCount()
    nums = [-1, -1, -1, 0, 0, 0, 3, 4, 6]
    nums_2 = [-3, -2, -1, -1, 1, 1, 5, 6]
    nums_3 = [0, 0, 0, 0, 0]

    print(maximum_count.maximum_count_v1(nums))
    print(maximum_count.maximum_count_v2(nums))

    print(maximum_count.maximum_count_v1(nums_2))
    print(maximum_count.maximum_count_v2(nums_2))
    print(maximum_count.maximum_count_v2(nums_3))