from typing import List

class SearchRotated():
    def search(self, nums: List[int], target: int) -> int:
        bottom, top = 0, len(nums) - 1
        
        while top >= bottom:
            mid = (top + bottom) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if nums[top] >= nums[mid] and nums[top] < target:
                    top = mid - 1 
                else:
                    bottom = mid + 1
            else:
                if nums[bottom] <= nums[mid] and nums[bottom] > target:
                    bottom = mid + 1 
                else:
                    top = mid - 1
        return -1
                    
                    
if __name__ == "__main__":
    searcher = SearchRotated()
    nums_1 = [4,5,6,7,0,1,2]
    nums_2 = [1, 3, 9, -5, -1, 0]
    
    print(searcher.search(nums_1, 0))
    print(searcher.search(nums_2, 0))