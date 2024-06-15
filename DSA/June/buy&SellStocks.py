# 121 Best Time to Buy and Sell Stocks, Easy

# Given an array prices where prices[i] is the price of a given stock on the ith day.
# Maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.

# Return Max Profit, if no profit return 0

# Input: prices = [7,1,5,3,6,4]
# Output: 5      
# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):
    