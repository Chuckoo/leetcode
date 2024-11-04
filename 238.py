class Solution:
    def productExceptSelf(self, nums: list) -> list:
        ans = [1 for i in range(len(nums))]
        curr = 1
        for i in range(len(nums)):
            ans[i] *= curr
            curr *= nums[i]
        curr = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= curr
            curr *= nums[i]
        return ans
    
nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))
