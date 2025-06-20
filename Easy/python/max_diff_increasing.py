from typing import List

class MaxDiffIncreasing():
    def maximum_difference(self, nums: List[int]) -> int:
        min, i = 0, 1
        largest_diff = -1
        
        while i < len(nums):
            if nums[min] >= nums[i]:
                min = i
            else:
                largest_diff = max(nums[i] - nums[min], largest_diff)
            i += 1
        return largest_diff