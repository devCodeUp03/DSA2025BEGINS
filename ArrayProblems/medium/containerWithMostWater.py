from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        water, max_water = 0, 0

        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                if height[i] <= height[j]:
                    water = height[i] * (j - i)
                else:
                    water = height[j] * (j - i)
                
                max_water = max(max_water, water)
        return max_water
    

obj = Solution()
max_water = obj.maxArea([1, 0])
print(max_water)