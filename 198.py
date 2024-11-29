class Solution:
    def rob(self, nums: int) -> int:
        if len(nums) <= 1:
            return nums[0]
        a = 0
        b = 0

        for i in range(len(nums)):
            temp = a
            a = max(a,b+nums[i])
            b = temp
        
        return a
              
        

nums = [1,2,3,1]
print(Solution().rob(nums))