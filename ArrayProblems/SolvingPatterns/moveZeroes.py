from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        latestNonZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[latestNonZero] = nums[latestNonZero], nums[i]
                latestNonZero +=1
        return nums



obj = Solution()
newArray = obj.moveZeroes([0,1,0,3,12])
print(newArray)