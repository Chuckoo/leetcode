class Solution:
    def minChanges(self, s: str) -> int:
        mid = len(s)//2
        if mid % 2 == 0:
            left = s[0:mid]
            right = s[mid:]
        else:
            left = s[0:mid-1] 
            right = s[mid-1:]
        if len(s) <= 2:
            return min(s.count("0"),s.count("1"))
        else:
            return self.minChanges(left) + self.minChanges(right)

s = "0000"  
print(Solution().minChanges(s))