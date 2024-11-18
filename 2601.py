class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        import math

        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        prev = 0
        for i in range(len(nums)):
            for j in range(nums[i],1,-1):
                if is_prime(j):
                    if nums[i] - j > prev:
                        nums[i] -= j
                        break
            prev = nums[i]
        prev = 0
        print(nums)
        for i in nums:
            if i <= prev:
                return False
            prev = i
        return True




            