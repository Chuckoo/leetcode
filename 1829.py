class Solution:
    def getMaximumXor(self, nums, maximumBit: int):
        ans = []
        rem = 0
        prefix_xor = nums[0]
        xor_mask = (1 << maximumBit) - 1
        for i in range(1,len(nums)):
            prefix_xor ^= nums[i]
        for i in range(len(nums)):
            ans.append(prefix_xor ^ xor_mask)
            prefix_xor ^= nums[len(nums) - i - 1]
        return ans

nums = [0,1,1,3]
maximumBit = 2
print(Solution().getMaximumXor(nums,maximumBit))

# print(bin((1 << 4) - 1))