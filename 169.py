from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # from collections import Counter
        # return Counter(nums).most_common(1)[0][0]

        #Ridiculous solution I found:
        # Uses https://www.cs.utexas.edu/~moore/best-ideas/mjrty/ (Linear time majority time algorithm)
        # Basically + if same elem, - if diff element, if count reaches 0 - change elem

        majorityNumber = nums[0]
        count = 1
        for n in nums[1:]:
            if count == 0:
                majorityNumber = n
                count += 1
            elif n == majorityNumber:
                count += 1
            else:
                count -= 1

        return majorityNumber


nums = [2,2,1,1,1,2,2]

print(Solution().majorityElement(nums))