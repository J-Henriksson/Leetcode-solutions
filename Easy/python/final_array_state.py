from typing import List
import heapq
class FinalArrayState(object):
    def get_final_state_bad_solution(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            temp_array = nums.copy()
            temp_array.sort()
            for i in range(len(nums)):
                if nums[i] == temp_array[0]:
                    temp_array[0] *= multiplier
                    nums[i] = temp_array[0]
                    break
        return nums
    
    def get_final_state_heap(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums_heap = []
        for i in range(len(nums)):
            heapq.heappush(nums_heap, (nums[i], i))
        
        for _ in range(k):
            value, index = nums_heap[0]
            value *= multiplier
            heapq.heapreplace(nums_heap, (value, index))
            nums[index] = value
        return nums
    
if __name__ == "__main__":
    array_state = FinalArrayState()
    nums = [2,1,3,5,6]
    print(array_state.get_final_state_heap(nums, 5, 2))