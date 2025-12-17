# from typing import List
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:

#        sumofk = 0
#        avg = 0
#        length = k
#        max_avg = 0

#     #    for i in range(k):
#     #        sum += nums[i]
#     #    avg = sum / k
        
#     #    return avg

#        for i in range(len(nums)):
#            while k in range(i, k):
#                sumofk += nums[j]
#            k+=1
#            avg = sumofk / length

#            max_avg = min(max_avg, avg)

#        return max_avg


from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum_ofk = sum(nums[:k])
        max_sum = window_sum_ofk

        for i in range(k, len(nums)):
            window_sum_ofk += nums[i]
            window_sum_ofk -= nums[i - k]
            max_sum = max(max_sum, window_sum_ofk)
        
        return max_sum / k







obj = Solution()
sum = obj.findMaxAverage([1,12,-5,-6,50,3], 4)
print(sum)
    







    



# nums = [1,12,-5,-6,50,3], k = 4
        