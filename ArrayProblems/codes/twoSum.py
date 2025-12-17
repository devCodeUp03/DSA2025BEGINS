from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        found = False
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    indices.append(i)
                    indices.append(j)
                    found = True
                    break
            if found:
                break
        return indices
    def twoSumHashMap(self, nums, target):
        mp = {}
        arrIndices = []
        for i, num in enumerate(nums):
            complement = target - num
            if complement in mp:
                arrIndices.append([mp[complement], i])
            mp[num] = i

        return arrIndices


obj = Solution()
# indices = obj.twoSum([3,2,4], 6)
# print(indices)

indices = obj.twoSumHashMap([3, 2, 4, 5, 1, 6], 7)
print(indices)
        