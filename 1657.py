class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False

        from collections import Counter
        s1 = Counter(word1)
        s2 = Counter(word2)

        s1_keys = s1.keys()
        s2_keys = s2.keys()

        s1_values = sorted(s1.values())
        s2_values = sorted(s2.values())

        if s1_keys == s2_keys and s1_values == s2_values:
            return True
        else:
            return False
            
word1 = "abbzzca"
word2 = "babzzcz"
  
print(Solution().closeStrings(word1,word2))