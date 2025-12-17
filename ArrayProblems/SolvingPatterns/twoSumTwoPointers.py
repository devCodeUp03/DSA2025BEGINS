def twoSumTwoPointers(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        s = nums[l] + nums[r]
        if s < target:
            l+=1
        elif s > target:
            r-=1
        else:
            return [l, r]
    return None

pair = twoSumTwoPointers([1, 2, 3, 4], 5)
print(pair)