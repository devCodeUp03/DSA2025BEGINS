from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowPointer:int = 0
        for fastPointer in range(1, len(nums)):
            if nums[slowPointer] != nums[fastPointer]:
                slowPointer+=1
                nums[slowPointer] = nums[fastPointer]
        
        return slowPointer + 1
    
obj = Solution()
k = obj.removeDuplicates([2,2, 3, 4])
print(k)

        