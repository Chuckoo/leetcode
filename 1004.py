class Solution:
    def longestOnes(self, nums, k: int) -> int:
        left = 0
        ans = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans


nums = [1,1,1,
        0,0,0,
        1,
        0,
        1,
        0,0
        ,1,1,1,1,
        0,
        1,
        0,
        1,1,1,
        0,
        1,1,
        0,
        1,
        0,
        1,1,
        0,
        1,1,
        0,
        1,1,1,
        0,0,0,
        1,
        0,0,0,
        1,1,1,1,
        0,0,1]
k = 10
print(Solution().longestOnes(nums,k))