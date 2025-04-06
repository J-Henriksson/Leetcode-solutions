class BinarySearch():
    """Quick implementation of binary search I made.
    """
    def binary_search(self, nums, target):
        top = len(nums) - 1
        bottom = 0
        while top >= bottom:
            mid = ((top - bottom) // 2) + bottom
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                bottom = mid + 1
            else:
                top = mid -1
        return -1 #In case the target doesn't exist in the list.
    
    def binary_search_recursive(self, nums, top, bottom, target):
        if top >= bottom:
            mid = ((top - bottom) // 2) + bottom

            if nums[mid] == target: #Base case.
                return mid
            elif nums[mid] < target:
                return self.binary_search_recursive(nums, top, mid + 1, target)
            else:
                return self.binary_search_recursive(nums, mid - 1, bottom, target)
        return -1 #Target not found.
    

if __name__ == "__main__":
    binary_search = BinarySearch()
    nums = [-1, 0, 1, 2, 3, 4, 9, 20, 23, 25, 29, 30, 33, 34, 79, 80]
    print(binary_search.binary_search(nums, 29))
    print(binary_search.binary_search_recursive(nums, len(nums) - 1, 0, 29))