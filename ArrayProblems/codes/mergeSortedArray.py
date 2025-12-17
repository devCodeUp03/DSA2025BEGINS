from typing import List
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         j = 0
#         for i in range(len(nums1)):
#             if len(nums2) == 0:
#                 return nums1
#             if nums1[i] > nums2[j]:
#                 nums1[i+1] = nums1[i]
#                 nums1[i] = nums2[j]
#                 j+=1
#             elif nums1[i] == 0 and i != 0:
#                 nums1[i] = nums2[j]
#                 j+=1        

#         return nums1
    
# obj = Solution()
# array = obj.merge([0], 0, [1],1 )
# print(array)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n -1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1

        while j >= 0:
            nums1[k] = nums2[j]
            j-=1
            k-=1
        return nums1
    
obj = Solution()
array = obj.merge([1, 0, 0], 1, [1, 2], 2)
print(array)


            

               
            
        