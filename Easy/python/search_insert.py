from typing import List
class SearchInsert():
    def search_insert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target or target < nums[i]: 
                return i
        return len(nums)
    
    def search_insert_binary_search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
    
if __name__ == "__main__":
    inserter = SearchInsert()
    nums_1 = [1,3,5,6,9]
    target = 10
    
    print(inserter.search_insert_binary_search(nums_1, target))