from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]


nums = [2,2,1,1,1,2,2]
   
print(Solution().majorityElement(nums))