class Solution:
    def compress(self, chars) -> int:
        count = 1
        prev = chars[0]
        ans = ""
        for i in chars[1:]:
            if i == prev:
                count += 1

            if i != prev:
                if count > 1:
                    ans +=  str(prev) + str(count)
                else:
                    ans += str(prev)
                prev = i
                count = 1
        if count > 1:
            ans += str(prev) + str(count)
        elif count == 1:
            ans += str(prev)
        chars.clear()
        for i in ans:
            chars.append(i)
        print(chars)
        return len(chars)
        

chars = ["a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]
print(Solution().compress(chars))