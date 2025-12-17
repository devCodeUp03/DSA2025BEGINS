from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writePointer = 0
        for scanPointer in range(len(nums)):
            if nums[scanPointer] != val:
                # nums[writePointer] = nums[scanPointer]
                nums[writePointer], nums[scanPointer] = nums[scanPointer], nums[writePointer]
                writePointer+=1
        return writePointer
    
    def removeAllElement(self, nums:List[int], val: int) -> int:
        resultArr = []
        for num in nums:
            if num != val:
                resultArr.append(val)
        return len(resultArr)
    
obj = Solution()
k = obj.removeElement([0,1,2,2,3,0,4,2], 2)
k2 = obj.removeAllElement([0,1,2,2,3,0,4,2], 2)
print(k, k2)
