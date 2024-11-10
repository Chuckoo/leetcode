class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height)-1
        maxi = 0
        while i < j:
            capacity = abs(j-i) * min(height[j],height[i])
            maxi = capacity if capacity > maxi else maxi
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return maxi

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))

# maxi = 0
# i, j = 0, 0
# capacity = 0
# for i in range(len(height)):
#     for j in range(len(height)):
#         capacity = abs(i-j) * min(height[i],height[j])
#         maxi = capacity if capacity > maxi else maxi
# return maxi

        