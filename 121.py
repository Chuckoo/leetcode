from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer approach
        buy = 0
        sell = 1
        n = len(prices)
        maxProf = 0
        while(sell<n):
            current = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                maxProf = max(current, maxProf)
            else:
                buy = sell
            
            sell += 1
        return maxProf

        # #O(n2) solution, need to make this faster
        # n = len(prices)
        # maxVal = float('-inf')
        # for i in range(n):
        #     for j in range(i,n):
        #         maxVal = maxVal if not (prices[j] - prices[i] > maxVal) else prices[j] - prices[i]
                
        # return maxVal if maxVal > 0 else 0
                
            
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))