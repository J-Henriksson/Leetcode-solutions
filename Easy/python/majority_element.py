class MajorityElement():

    def majority_element(self, nums):
        """Finds the number within a list that comprises more than half of the elements. The question presupposed that all inputs would contain an element like this, in that case
        that number is returned. Otherwise -1 is returned.

        Analysis: Cool solution that utilizes hashmaps. Time complexity is probably O(n) but could be O(1) depending on the list size Ig.
        Runtime: Beats 9.32% :(
        Memory: Beats 90.34%
        
        Args:
            nums (list): list of numbers.

        Returns:
            int: The number that occurs in more than half of the list, or -1 if no such number is found.
        """
        occurrences = {}

        for number in nums:
            if number in occurrences:
                occurrences[number] = occurrences.get(number) + 1
            else:
                occurrences.update({number: 1})
            if occurrences.get(number) > len(nums) / 2:
                return number
        return -1 #If no majority element exists.
    

    def majority_element_v2(self, nums):
        """Same problem as the other method.

        Analysis: Really simple and elegant solution. O(n) time complexity.
        Runtime: Beats 100%
        Memory: Beats 31.08%

        Args:
            nums (list): list of numbers.

        Returns:
            int: The majority number.
        """
        nums.sort()
        return nums[len(nums) // 2]
    
    def boyer_moore(self, nums):
        """Same problem.

        Analysis: Cool algorithm that's very intuitive once you understand it.
        Runtime: Beats 73.91&
        Memory: 90.33%

        Args:
            nums (list): List of numbers.

        Returns:
            int: The majority number.
        """
        contender = nums[0]
        count = 0
        for number in nums:
            if count == 0:
                contender = number
                count = 1
            elif number == contender:
                count += 1
            else:
                count += -1
        return contender


if __name__ == "__main__":
    majority_element = MajorityElement()
    nums = [1,2,2,3,1,1,1,1]

    print(majority_element.majority_element(nums))
    print(majority_element.majority_element_v2(nums))
    print(majority_element.boyer_moore(nums))