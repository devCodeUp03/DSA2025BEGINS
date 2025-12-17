# def productOfArr(nums): # quadratic time complexity as well as linear space complexity
#     productArr = []
#     for i in range(len(nums)):
#         product = 1
#         for j in range(len(nums)):
#             if i == j:
#                 continue
#             product *= nums[j]
#         productArr.append(product)
#     return productArr


# productArr = productOfArr([1, 2, 3, 4])
# print(productArr)

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size

        prefix = 1
        for i in range(size):
            result[i] *= prefix
            prefix *= nums[i]


        suffix = 1
        for i in range(size - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
    
obj = Solution()
newArray = obj.productExceptSelf([1, 2, 3, 4])
print(newArray)