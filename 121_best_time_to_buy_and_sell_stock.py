
'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''

from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = inf

        for price in tuple(prices):
            if price < buy_price:
                buy_price = price
            if profit < price - buy_price:
                profit = price - buy_price

        return profit
