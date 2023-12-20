from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer approach
        #basically the prev sell questio, but a little modification to the code
        buy = 0
        sell = 1
        n = len(prices)
        maxProf = 0
        maxi = 0
        while(sell<n):
            if prices[buy] < prices[sell] and prices[sell] - prices[buy] > maxi:
                maxi = prices[sell] - prices[buy]
                sell += 1
            else:
                maxProf += maxi
                maxi = 0
                buy = sell
                sell +=1
            
        maxProf += maxi

        return maxProf
                
            
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))
prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))