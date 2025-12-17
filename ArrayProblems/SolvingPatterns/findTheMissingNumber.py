from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        xor_all = 0
        xor_num = 0

        for i in range(size+1):
            xor_all ^= i

        for num in nums:
            xor_num ^= num

        return xor_all ^ xor_num
    
obj = Solution()
missingNumber = obj.missingNumber([3, 0, 1])
print(missingNumber)