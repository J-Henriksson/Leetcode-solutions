from typing import List

class BuySellStock():
    def max_profit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return max_profit
    

if __name__ == "__main__":
    buy_sell = BuySellStock()
    prices_1 = [7,1,5,3,6,4]
    prices_2 = [7,6,4,3,1]
    
    print(buy_sell.max_profit(prices_1))
    print(buy_sell.max_profit(prices_2))