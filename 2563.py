class Solution:
    def countFairPairs(self, nums: int, lower: int, upper: int) -> int:
        from bisect import bisect_left, bisect_right
        nums.sort()
        ans = 0
        for i in range(len(nums)-1):
            low = bisect_left(nums, lower - nums[i], i+1)
            up = bisect_right(nums, upper - nums[i], i+1)
            ans += up-low
        return ans
            


nums = [0,1,7,4,4,5] 
lower = 3
upper = 6  
print(Solution().countFairPairs(nums,lower,upper))

