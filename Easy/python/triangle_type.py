from typing import List

class TriangleType():
    def triangle_type(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or nums[1] + nums[2] <= nums[0]:
            return "none"
        if nums[0] == nums[1] and nums[0] == nums[2] and nums[0] != 0:
            return "equilateral"
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"
        return "scalene"
        