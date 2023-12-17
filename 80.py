class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        valueReplacePointer = 0
        
        for n in nums:
            if valueReplacePointer < 2 or n > nums[valueReplacePointer - 2]:
                nums[valueReplacePointer] = n
                valueReplacePointer+=1
        return valueReplacePointer
    
    #Read the list
    #If list element is greater than 2 before, move on
    #else keep the pointer on the third replica
    #when new elem is encountered, it will replace where pointer has stopped
    
    #Notes:
    #Think 2 pointers