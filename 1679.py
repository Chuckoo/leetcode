from collections import Counter
class Solution:
    def maxOperations(self, nums, k) -> int:
        ans = 0
        counts = Counter(nums)
        for i in set(nums):
            while counts.get(i,0) > 0 and counts.get(k-i,0) > 0:
                if i == k-i:
                    if counts.get(i,0) <= 1:
                        break
                ans += 1
                counts[i] -= 1
                counts[k-i] -= 1

        return ans









        # count = 0
        # i,j = 0,0
        # while i < len(nums):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == k-nums[j]:
        #             count += 1
        #             temp = nums[j]
        #             nums[j] = nums[i+1]
        #             nums[i+1] = temp
        #             i += 1
        #             break
        #     i+=1
        # return count


        
nums = [3,1,3,4,3]
k = 6
print(Solution().maxOperations(nums,k))