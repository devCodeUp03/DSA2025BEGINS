from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        for num in nums1:
            result.append(num)
        
        for num in nums2:
            result.append(num)        

        result.sort()

        if len(result) % 2 == 0:
            mid = len(result) // 2
            median = (result[mid-1] + result[mid]) / 2
            return median
        else:
            mid = len(result) // 2
            median = result[mid]
            return median
        
obj = Solution()
result = obj.findMedianSortedArrays([1, 2], [3, 4])
print(result)