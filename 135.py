from typing import List 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalSum = 0
        currentSum = 0
        start= 0

        if(sum(gas)<sum(cost)):
            return -1
        
        for i in range(len(gas)):
            totalSum += gas[i] - cost[i]
            currentSum += gas[i] - cost[i]
            if currentSum < 0:
                currentSum = 0
                start = i + 1
        
        return start


        


gas = [2,3,4]
cost = [3,4,3]
print(Solution().canCompleteCircuit(gas,cost))