class Solution:
    def longestOnes(self, nums, k: int) -> int:
        left = 0
        zero_count = 0
        ans = 0
        for right in range(left,len(nums)):
            if nums[right] == 0:
                zero_count += 1

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2 
print(Solution().longestOnes(nums,k))