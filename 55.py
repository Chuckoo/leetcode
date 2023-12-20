from typing import List 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxRange = 0
        for i, n in enumerate(nums):
            if i > maxRange:
                return False
            maxRange = max(maxRange,i+n)
        return True


nums = [3,2,1,0,4]
print(Solution().canJump(nums))