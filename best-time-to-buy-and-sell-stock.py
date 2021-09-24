# LINK TO LEETCODE: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
from typing import List
# Unfinished !
def maxProfit(prices: List[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit
    by choosing a single day to buy one stock and choosing a different day in the future to sellthat stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Idea:
        highest_price = (price, idx)    - Store highest price along with the index in the array
        lowest_price = (price, idx)     - Store lowest price along with the index in the array
                                        - Initial value of price in tuple should be prices[0]

        for price in prices:     - loop through prices
            - Set lowest price to current price if it is lower 
            
            if price < lowest_price[i]:
                lowest_price = (price, i)
            if price > highest_price[i]:
                highest_price = (price, i)
            
        if lowest_price >= highest_price:
            return 0
        return highest_price[0] - lowest_price[0]

    Example 1:

        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:

        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transactions are done and the max profit = 0.
    """
    if not prices: return 0
    highest_price = (prices[0], 0)
    lowest_price = (prices[0], 0) 
    possibility = None
    for i, price in enumerate(prices):
        print("highest price", highest_price)
        print("lowest price", lowest_price)
        if lowest_price[0] < highest_price[0] and lowest_price[1] < highest_price[1]: 
            if not possibility:
                possibility = (highest_price[0], lowest_price[0])
            elif possibility[0] - possibility[1] < highest_price[0] - lowest_price[1]:
                possibility = (highest_price[0], lowest_price[0])
                
        # Reset highest price if lowest price comes after
        if lowest_price[1] > highest_price[1]: 
            highest_price = (0, -1)
        if price < lowest_price[0]: 
            lowest_price = (price, i)
        if price > highest_price[0]: 
            highest_price = (price, i)

    if lowest_price[0] < highest_price[0] and lowest_price[1] < highest_price[1]: 
        if not possibility:
            possibility = (highest_price[0], lowest_price[0])
        elif possibility[0] - possibility[1] < highest_price[0] - lowest_price[1]:
            possibility = (highest_price[0], lowest_price[0])
            
    return 0 if not possibility else possibility[0] - possibility[1]

# print("SHOULD BE 5",maxProfit([7,1,5,3,6,4]))
# print("SHOULD BE 0",maxProfit([3,2,6,5,0,3]))
print("SHOULD BE 2, IS:",maxProfit([2,1,2,1,0,1,2]))