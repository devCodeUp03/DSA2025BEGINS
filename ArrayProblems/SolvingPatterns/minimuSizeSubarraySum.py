from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_window = 0
        left = 0
        min_length = float('inf')

        for right in range(len(nums)):
            sum_window += nums[right]

            while sum_window >= target:
                min_length = min(min_length, right - left + 1)
                sum_window -= nums[left]
                left+=1
        
        return 0 if min_length == float('inf') else min_length
