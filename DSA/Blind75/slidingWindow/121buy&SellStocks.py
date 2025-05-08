# 121 Best Time to Buy and Sell Stocks, Easy

'''
Given an array prices where prices[i] is the price of a given stock on the ith day.
Maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return Max Profit, if no profit return 0

Input: prices = [7,1,5,3,6,4]
Output: 5      
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

def maxProfit(prices):
    '''
    buy = 0
    sell = len(prices)-1
    output = 0
    while buy < sell:
        if prices[buy+1] < prices[buy]:
            buy += 1
        if prices[sell-1] < prices[sell]:
            sell -= 1
        
        if (prices[sell] - prices[buy]) > 0:
            output = output + (prices[sell] - prices[buy])
            return output
        else:
            return 0
    '''
    buy, sell = 0, 1
    maxP = 0
    
    #while right pointer (sell) has isnt at the end of array
    while sell <len(prices):
        if prices[buy] < prices[sell]: 
            #calculate profit
            profit = prices[sell] - prices[buy]
            maxP = max(maxP, profit)
        else: #buy price is higher than sell price
            buy = sell #since sell is lower than buy, we move to it
            
        sell += 1 #keep moving the sell pointer forward, until it reaches end of list and will not go to while loop
    return maxP