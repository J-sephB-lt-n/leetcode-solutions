"""
121. Best Time to Buy and Sell Stock
Easy

    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104

My solution (high-level logic):
    * use 2 pointers: buy (left) and sell (right)
    * start [buy] pointer at index 0
    * start [sell] pointer at index 1
    * iterate [sell] pointer through all values in list, at each step:
        o keep track of global min [sell] value seen
        o calculate profit (remember global max profit achieved)
        o if [sell] value < global_min_sell_value_seen: update [sell] pointer to this value
    * if max profit achieved is under 0, return 0
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_idx = 0
        max_profit_seen = 0
        for sell_idx, sell_value in enumerate(prices[1:], start=1):
            profit = sell_value - prices[buy_idx]
            if profit > max_profit_seen:
                max_profit_seen = profit
            if sell_value < prices[buy_idx]:
                buy_idx = sell_idx
        return max_profit_seen


import random

random_test_case = random.sample(list(range(1, 11)), k=10)
print(random_test_case)
Solution().maxProfit(random_test_case)
