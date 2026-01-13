from typing import List

class Permutations():
    
    def permute(self, nums: List[int]) -> List[int]:
        self.permutations = []
        self.dfs(0, nums)
        return self.permutations
        
    def dfs(self, pos: int, nums: List[int]):
        if pos == len(nums) - 1:
            self.permutations.append(nums[:])
            return
        for i in range(pos, len(nums)):
            #change
            temp = nums[pos]
            nums[pos] = nums[i]
            nums[i] = temp
            self.dfs(pos + 1, nums)
            #reset
            nums[i] = nums[pos]
            nums[pos] = temp

if __name__ == "__main__":
    permuter = Permutations()
    nums = [1,2,3]
    
    print(permuter.permute(nums))