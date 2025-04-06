class ThreeSum():

    def second_solution(self, nums):
        sum_numbers = set()
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while k > j:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    sum_numbers.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return list(sum_numbers)
    
if __name__ == "__main__":
    sorted_numbers1 = [-1,0,1,2,-1,-4]
    three_sum = ThreeSum()
    
    print(three_sum.second_solution(sorted_numbers1))
        

        