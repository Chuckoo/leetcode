class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[-1::-1])

print(Solution().reverseWords("the  sky   is  blue  "))