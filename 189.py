from typing import List

class Solution:
    def reversed(self, nums, left, right):
        while(left < right):
            temp = nums[left] 
            nums[left] = nums[right] 
            nums[right] = temp
            left += 1
            right -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n #reducing the no. of rotations
        
        #reverse 0 to n-k-1
        self.reversed(nums,0,n-k-1)
        #reverse n-k-1 to n-1
        self.reversed(nums,n-k,n-1)
        #reverse all
        nums.reverse()
    # def rotate(self, nums: List[int], k: int) -> None:
    #     if k == 0:
    #         print(nums)
    #         return None
        
    #     nums = nums[-1:] + nums[:-1]
    #     self.rotate(nums,k%len(nums)-1)
    #     #this works, but wont accept it cuz apparently its not "in place"

nums = [-1,-100,3,99]

k = 2
Solution().rotate(nums,k)
print(nums)
