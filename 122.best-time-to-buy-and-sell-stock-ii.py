#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) < 2: return 0
        # price_to_buy = prices[0]
        # price_to_sell = 0
        # profit = 0
        # for i in range(1,len(prices)):
        #     if prices[i] < price_to_sell:
        #         profit += price_to_sell - price_to_buy
        #         price_to_sell = 0
        #         price_to_buy = prices[i]
        #     elif prices[i] < price_to_buy:
        #         price_to_buy = prices[i]
        #     elif prices[i] > price_to_sell:
        #         price_to_sell = prices[i]
        # if price_to_sell > price_to_buy:
        #     profit += price_to_sell - price_to_buy
        # return profit
        if len(prices) < 2: return 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
        return profit
        

