from typing import List

def twoSumHashMap(nums: List[int], target: int) -> List[int]:
 
    mp = {} #value -> index
    for i, num in enumerate(nums): #enumerate gives index and value
        complement = target - num
        if complement in mp:
            return [mp[complement], i]
        mp[num] = i

nums = [1, 2, 2, 3, 4, 6]
target = 8
pair = twoSumHashMap(nums, target)
print(pair)

