def calculateFrequency(nums):
    mp = dict()
    for num in nums:
        mp[num] = mp.get(num, 0) + 1
    print(mp)

calculateFrequency([1, 2, 2, 3, 3, 4, 1, 1, 4])