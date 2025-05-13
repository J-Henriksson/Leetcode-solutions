from typing import List

class RotateArray(object):
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        result = nums.copy()

        for i in range(len(nums)):
            index = (i + k) % len(nums)
            result[index] = nums[i]
        for i in range(len(nums)):
            nums[i] = result[i]
    
    #Better and cooler solution
    def rotate_alternate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]

if __name__ == "__main__":
    rotateor = RotateArray()
    nums = [1,2,3,4,5,6,7]
    print(nums[len(nums) - 1: len(nums) - 2 - 1: -1])
    rotateor.rotate_alternate(nums, 2)
    print(nums)