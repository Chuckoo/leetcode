class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        prev = word[0]
        ans = ""
        for i in word[1:]:
            if i == prev:
                count += 1
            
            if count >= 9:
                ans += str(count) + str(prev)
                count = 0
                continue

            if i != prev:
                if count != 0:
                    ans += str(count) + str(prev)
                prev = i
                count = 1
        if count > 0:
            ans += str(count) + str(prev)
        return ans




word = "aaaaaaaaay"
print(Solution().compressedString(word))