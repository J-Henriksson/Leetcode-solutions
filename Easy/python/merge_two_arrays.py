from typing import List

class MergeTwoArrays():
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1   

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k, j = k - 1, j - 1
            else:
                nums1[k] = nums1[i]
                k, i = k - 1, i - 1
        if i < 0:
            if len(nums1) == 1:
                nums1[0] = nums2[0]
            else:
                nums1[:k + 1] = nums2[:j + 1]
 


    def merge_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        if i > len(nums1) - 1:
                return merged + nums2[j:]
        elif j > len(nums2) - 1:
            return merged + nums1[i:]

if __name__ == "__main__":
    merger = MergeTwoArrays()
    list1 = [1,2,9,0]
    list2 = [3]

    list3 = [1,2,3,7,9,0,0,0]
    list4 = [3,8,9]

    list5 = [0]
    list6 = [1]

    list7 = [2,0]
    list8 = [1]

    #merger.merge(list1, 3, list2, 1)
    #merger.merge(list3, 5, list4, 3)
    #merger.merge(list3, 5, list4, 3)
    #merger.merge(list5, 0, list6, 1)
    merger.merge(list7, 1, list8, 1)

    #print(list1)
    #print(list3)
    #print(list5)
    print(list7)