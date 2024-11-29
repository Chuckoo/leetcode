class Solution:
     def decrypt(self, code, k: int):
        ans = []
        n = len(code)
        if k == 0:
            for i in range(n):
                code[i] == 0
                ans.append(0)
            return ans

        window = 0

        if k > 0:
            for j in range(1,k+1):
                window += code[j % n]
            ans.append(window)
            for i in range(1,n):
                window += code[(k + i) % n]
                window -= code[i]
                ans.append(window)
            return ans
            
        if k < 0:
            for j in range(1,abs(k)+1):
                window += code[(-j) % n]
            ans.append(window)
            for i in range(1,n):
                window += code[-i+k % n]
                window -= code[-i]
                ans.insert(1,window)
            return ans

code = [2,4,9,3]
k = -2

print(Solution().decrypt(code,k))