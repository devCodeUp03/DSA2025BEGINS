def singleNumber(nums):
    for i in range(len(nums)):
        notFound = False
        for j in range(len(nums)):
            if nums[i] == nums[j] and i != j:
                notFound = True
                break
        if not notFound:
            return nums[i]
        
        


single = singleNumber([4, 1, 2, 2, 4, 3, 3])
print(single)
  