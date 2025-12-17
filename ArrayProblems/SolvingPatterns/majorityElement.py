from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        majorityKey = next(iter(mp))
        majorityValue = mp[majorityKey]
        # print(majorityKey, majorityValue)

        for key, value in mp.items():
            print(key, value)
            # print(majorityKey, majorityValue)
            if value > majorityValue:
                print("hi")
                majorityValue = value
                majorityKey = key
        
        return majorityKey
        # return mp


obj = Solution()
mp = obj.majorityElement([3, 2, 3])
print(mp)

        