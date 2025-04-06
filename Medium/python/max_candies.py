from typing import List

class MaxCandies():
    def maximum_candies(self, candies: List[int], k: int) -> int:
        candies.sort()
        top = candies[len(candies) - 1]
        bottom = 1
        result = 0

        while top >= bottom:
            mid_candies = (top + bottom) // 2
            mid_k = self.kids_per_candy(candies, mid_candies)
            if mid_k < k:
                top = mid_candies - 1
            else:
                result = mid_candies
                bottom = mid_candies + 1
        return result
    
    def kids_per_candy(self, candies: List[int], candy: int) -> int:
        people = 0
        for pile in candies:
            people += pile // candy
        return people
    
if __name__ == "__main__":
    max_candies = MaxCandies()
    candies_1 = [5,8,6]

    print(max_candies.maximum_candies(candies_1, 3))