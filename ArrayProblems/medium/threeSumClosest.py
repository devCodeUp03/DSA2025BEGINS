from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = float('inf')
        for i in range(n):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    closest = nums[i] + nums[j] + nums[k]
                    if abs(target - closest) < abs(target - closest_sum):
                        closest_sum = closest
        return closest_sum



obj = Solution()
closest_sum = obj.threeSumClosest([0,0,0], 1)
print(closest_sum)