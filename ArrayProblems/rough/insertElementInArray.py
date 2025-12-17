def insertElement(nums, el):
    for i in range(len(nums) - 1, 0, -1):
        nums[i] = nums[i-1]
    nums[0] = el

nums = [2, 3, 4, 5]
insertElement(nums, 1)
print(nums)