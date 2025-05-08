""" 121 Buy and Sell Stocks, Easy
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0."""

class Solution:
    def profit(self, prices : [int]) -> int:
        left, right = 0, 1
        max_p = 0
        
        while right < len(prices):
            """WRONG
            if prices[left] > prices[right]:
                left = right
                right += 1
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            elif prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
                right += 1
                
        return max_profit
        """
            #check if profitable
            if prices[left] <= prices[right]:
                profit = prices[right] - prices[left]
                max_p = max(profit, max_p)
            else:
                left = right
            right += 1
        return max_p
                


sol = Solution()
result1 = sol.profit([10,1,5,6,7,1]) #6, buy profit[1] = 1 and sell profit[4] = 7 profit = sell - buy = 6
print(result1)