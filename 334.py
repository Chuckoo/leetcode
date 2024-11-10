class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = float("inf")
        second = float("inf")
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

nums = [0,4,2,1,0,-1,-3]
print(Solution().increasingTriplet(nums))