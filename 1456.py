class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])
        i = 0
        count = 0
        for letter in s[i:k+i]:
            if letter in vowels:
                    count += 1
        ans = count
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowels:
                count -= 1
            if s[i+k-1] in vowels:
                count += 1
            if count == k:
                return count
            ans = max(count,ans)
        return ans
        
    
s = "tryhard"
k = 4  
print(Solution().maxVowels(s,k))