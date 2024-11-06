class Solution:
    def canSortArray(self, nums) -> bool:
        def isSetBit(x,y):
            if bin(x).count("1") == bin(y).count("1"):
                return True
            else:
                return False
        i = 0
        j = 0
        for i in range(len(nums)):
            swapped = False
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    if isSetBit(nums[j],nums[j+1]):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        swapped = True
                    else:
                        return False
            if (swapped == False):
                break    
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return False
            
        return True

        
nums = [1,2,3,4,5]
print(Solution().canSortArray(nums))
# import heapq
# pq = []
# heapq.heappush(pq, 3)
# heapq.heappush(pq, 5)
# heapq.heappush(pq, 2)
# print(heapq.heappop(pq))