from typing import List
import math

class KokoEatingBananas():
    def banana_eater(self, piles: List[int], h: int) -> int:
        piles.sort()
        top = piles[len(piles) - 1]
        bottom = 1 
        result = -1

        while top >= bottom:
            mid = (top + bottom) // 2
            mid_time = self.time_to_eat_bananas(piles, mid)
            if mid_time <= h:
                result = mid
                top = mid - 1
            else:
                bottom = mid + 1
        return result
    
    def time_to_eat_bananas(self, piles: List[int], speed: int) -> int:
        sum = 0
        for pile in piles:
            sum += math.ceil(pile / speed)
        return sum
    
if __name__ == "__main__":
    banana_eater = KokoEatingBananas()
    piles = [3,6,7,11]
    piles_2 = [58,11,29,4,20]
    piles_3 = [312884470]

    print(banana_eater.banana_eater(piles, 8))
    print(banana_eater.banana_eater(piles_2, 6))
    print(banana_eater.banana_eater(piles_3, 312884469))