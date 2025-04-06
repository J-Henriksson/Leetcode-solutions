class RemoveElement():

    def remove_element(self, nums, val):
        """Moves all the numbers that match the value to the back of the list.
        Kind of a convoluted method, basically it goes through each element and if it encounters
        the value to be removed the position is stored in index. And next time it encounters
        a non value element the positions are switched and the loop is moved back to one place after
        the index. Index is set to len(nums) so that the method works with lists that don't
        contain the value as well.

        Analysis: Works fine but could be improved for readability. Time complexity of O(n) (best case).
        Runtime: Beats 100%
        Memory: Beats 80%

        Args:
            nums (list): List of numbers.
            val (int): The number to be removed (moved to the back).

        Returns:
            index (int): The amount of numbers in the list that aren't val.
        """
        index = len(nums)
        number = 0

        while number < len(nums):
            if nums[number] != val and index != len(nums):
                nums[index] = nums[number]
                nums[number] = val
                number = index
                index = len(nums)
            elif index == len(nums) and nums[number] == val:
                index = number
            number += 1
        return index
    

    def remove_element_v2(self, nums, val):
        """Simpler and more readable solution. Loops through each element if the element
        doesn't match val it's moved to the front of the list.

        Analysis: Way more elegant and most importantly readable.
        Runtime: Beats 100%
        Memory: Beats 51.39%

        Args:
            nums (list): List of numbers.
            val (int): The number to be removed (moved to the back).

        Returns:
            index (int): The amount of numbers in the list that aren't val.
        """
        index = 0

        for number in range(len(nums)):
            if nums[number] != val:
                nums[index] = nums[number]
                index += 1
            return index
    

if __name__ == "__main__":
    remove_element = RemoveElement()
    nums = [3, 1, 3, 2, 7, 4, 3, 5, 8]
    nums_2 = [0,1,2,2,3,0,4,2]

    print(remove_element.remove_element_v2(nums, 3))
    print(nums)
    print(remove_element.remove_element_v2(nums_2, 2))
    print(nums_2)