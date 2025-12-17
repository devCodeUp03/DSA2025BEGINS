from typing import List

def bubbleSort(nums: List[int]) -> List[int]:
    sorted = True
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            print("hi")
            if nums[j] > nums[j+1]:
                # print("hi")
                sorted = False
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if sorted:
            break
        
    return nums


nums = bubbleSort([11, 12, 22, 25, 64])
# nums = bubbleSort([64, 25, 12, 22, 11])
print(nums)