class Solution:
    def minimumSubarrayLength(self, nums, k) -> int:
        left = 0
        ans = float("inf")
        val = nums[0]
        ones = [0 for _ in range(32)]
        temp = 0
        right = 0
        for right in range(len(nums)):

            val |= nums[right]
            for i in range(32):
                if nums[right] & (1 << i):
                    ones[i] += 1
            
            while val >= k and left <= right:
                ans = min(ans,right-left+1)

                for i in range(32):
                    if nums[left] & (1 << i):
                        ones[i] -= 1
    
                    if ones[i] > 0:
                        temp |= (1 << i)

                left += 1
                val = temp
                temp = 0 


        if ans != float('inf'):
            return ans
        else:
            return -1


                
            




nums = [1,2,32,21]
k = 55
print(Solution().minimumSubarrayLength(nums, k))