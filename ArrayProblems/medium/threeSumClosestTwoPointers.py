from typing import List
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         closest_sum = float('inf')
#         nums.sort()
#         n = len(nums)

#         for i in range(n-1):
#             l = i + 1
#             r = n - 1
#             while l < r:
#                 closest = nums[i] + nums[l] + nums[r]
#                 if abs(target - closest) < abs(target - closest_sum):
#                     closest_sum = closest
#                 if closest_sum <= target:
#                     l+=1
#                 else:
#                     r-=1
#         return closest_sum
    


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float('inf')
        nums.sort()
        n = len(nums)

        for i in range(n-1):
            l = i + 1
            r = n - 1
            while l < r:
                closest = nums[i] + nums[l] + nums[r]
                if abs(target - closest) <= abs(target - closest_sum):
                    closest_sum = closest
                if closest < target:
                    l+=1
                elif closest > target:
                    r-=1
                else:
                    return closest                

        return closest_sum
obj = Solution()
closest_sum = obj.threeSumClosest([-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38]
, 78)
print(closest_sum)
        