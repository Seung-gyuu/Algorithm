class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # #choosing a single day to buy one stock and choosing a different day to sell that stock
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit