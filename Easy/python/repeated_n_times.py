from typing import List

class RepeatedNTimes():
    
    def repeated_times(self, nums: List[int]) -> int:
        map = set()
        
        for num in nums:
            if num in map:
                return num
            map.add(num)        
        return 0
    
    
if __name__ == "__main__":
    repeated = RepeatedNTimes()
    nums = [1,2,3,3]
    nums_1 = [2,1,2,5,3,2]
    nums_2 = [5,1,5,2,5,3,5,4]
    
    print("{}, {}, {}".format(repeated.repeated_times(nums), repeated.repeated_times(nums_1), repeated.repeated_times(nums_2)))