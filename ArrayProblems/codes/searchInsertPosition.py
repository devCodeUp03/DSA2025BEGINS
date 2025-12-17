from typing import List

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
            
#         for i in range(len(nums)):
#             if nums[0] > target:
#                 return 0
#             if nums[len(nums) - 1] < target:
#                 return len(nums)
#             if nums[i] < target and nums[i+1] > target:
#                 return i + 1
            
# obj = Solution()
# index = obj.searchInsert([1, 2, 4, 6, 7], 5)

# print(index)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if nums[mid] > target:
            return mid
        else:
            return mid + 1
        
    def searchInsertLinear(self, nums: List[int], target: int) -> int:
        j = 0
        for i, num in enumerate(nums):
            if num == target:
                return i
        
        for i, num in enumerate(nums):
            if target < nums[0]:
                return 0
            if target > nums[len(nums) - 1]:
                return len(nums)
            if nums[i] < target < nums[i+1]:
                return i + 1



obj = Solution()
# k = obj.searchInsert([1, 2, 4, 6, 7], 5)
k = obj.searchInsertLinear([1, 2, 4, 5, 7], 2)
print(k)
