class MaximumSubarray():

    def maximum_subarray(self, nums):
        sum = 0
        largest_sum = nums[0]
        for number in range(0, len(nums)):
            sum += nums[number]
            if sum > largest_sum:
                largest_sum = sum
            if sum < 0:
                sum = 0
        return largest_sum

if __name__ == "__main__":
    maximum_subarray = MaximumSubarray()
    nums_1 = [-2,1,-3,4,-1,2,1,-5,4]
    nums_2 = [1]
    nums_3 = [5,4,-1,7,8]
    nums_4 = [-4,-7,-20,-1, 0]
    nums_5 = [-2,1]
    nums_6 = [5,4,-1,7,8]

    print(maximum_subarray.maximum_subarray(nums_1))
    print(maximum_subarray.maximum_subarray(nums_2))
    print(maximum_subarray.maximum_subarray(nums_3))
    print(maximum_subarray.maximum_subarray(nums_4))
    print(maximum_subarray.maximum_subarray(nums_5))
    print(maximum_subarray.maximum_subarray(nums_6))