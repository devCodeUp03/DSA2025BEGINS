from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        thatNumber = 0

        for num in nums:
            thatNumber ^= num
        return thatNumber