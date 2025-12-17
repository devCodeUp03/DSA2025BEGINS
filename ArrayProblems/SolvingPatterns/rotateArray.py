# def rotateArray(nums, k):
#     for i in range(k):
#         lastElement = nums[len(nums) - 1]
#         for j in range(len(nums) - 1, 0, -1):
#             nums[j] = nums[j-1]
#         nums[0] = lastElement
#     return nums

# nums = rotateArray([1, 2, 3, 4, 5], 3)
# print(nums)

# There is a trick 
# 1. reverse the entire array
# 2. reverse the first k elements
# 3. reverse the remaining elements n - k 

def rotateArrWithExtraSpace(nums, k):
    n = len(nums)
    newArr = [0] * n
    for i in range(n):
        r = (i + k) % n 
        newArr[r] = nums[i]
    for i in range(n):
        nums[i] = newArr[i]
    return nums

nums = rotateArrWithExtraSpace([1,2,3,4,5], 2)
print(nums)

            