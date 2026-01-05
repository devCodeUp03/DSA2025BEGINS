# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         stack = []
#         indices = []
#         nge = {}
#         if len(nums) == 1:
#             return [-1]
        
#         for i in range(len(nums)):
#             while stack and nums[i] > stack[-1]:
#                 nge[stack.pop()] = nums[i]
#                 indices.pop()
            
#             stack.append(nums[i])
#             indices.append(i)
        

#         for i in indices:
#             j = 0
#             while j < i:
#                 if stack and nums[j] > nums[i]:
#                     nge[stack.pop()] = nums[j]
#                     break
#                 j+=1
#             if stack:
#                 nge[stack.pop()] = -1
        

#         return [nge[num] for num in nums]


# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [-1] * n
#         stack = []  # stores indices

#         # Traverse the array twice to simulate circular behavior
#         for i in range(2 * n):
#             curr = nums[i % n]

#             while stack and nums[stack[-1]] < curr:
#                 idx = stack.pop()
#                 res[idx] = curr

#             if i < n:
#                 stack.append(i)

#         return res
