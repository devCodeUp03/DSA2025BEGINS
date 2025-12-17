from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        water = min(height[l], height[r]) * (r - l)
        max_water = water

        while l < r:
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
            water = min(height[l], height[r]) * (r - l)
            max_water = max(max_water, water)
        
        return max_water


obj = Solution()
max_water = obj.maxArea([1,8,6,2,5,4,8,3,7])
print(max_water)

    