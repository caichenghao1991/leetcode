# 714. Best Time to Buy and Sell Stock with Transaction Fee           need rework
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res, min_price = 0, prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - fee > min_price:
                res += (prices[i] - fee - min_price)
                min_price = prices[i] - fee
                # let next_higher-cur_min-fee = curr-cur_min-fee+(next_higher-(cur-fee)-fee)
        return res
