from typing import List

class FinalPrices(object):
    def final_prices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, value in enumerate(prices):
            while stack and prices[stack[-1]] >= value:
                prices[stack[-1]] -= value
                stack.pop()
            stack.append(i)
        return prices

if __name__ == "__main__":
    final_prices = FinalPrices()
    prices = [10,1,1,6]

    print(final_prices.final_prices(prices))
