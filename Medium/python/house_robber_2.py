from typing import List

class HouseRobber2():
    def rob_line(self, nums: List[int]) -> int:
        #Same as max step money problem, but without a limit on how big steps you can take.
        #Create a list were each index as the max amount that can be stolen if you start from that house.
        #Each entry will be either be equal to itself or the largest other entry that isn't directly adjacent.
        
        max_amount = [nums[0]]
        best_house = 0
        for i in range(1, len(nums)):
            max_amount.append(nums[i] + best_house)
            best_house = max(max_amount[i - 1], best_house)
        return max(max_amount[-1], best_house)
    
    def rob_circle(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_line(nums[0:len(nums) - 1]), self.rob_line(nums[1:len(nums)]))