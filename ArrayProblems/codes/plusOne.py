from typing import List
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         if digits[len(digits) - 1] == 9:
#             digits[len(digits) - 1] = 1
#             digits.append(0)
#             return digits
#         else: 
#             digits[len(digits) -1]+=1
#             return digits
        

# obj = Solution()
# newArray = obj.plusOne([4,3,2,9])
# print(newArray)


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(map(str, digits)))
        integer+=1

        digitsPlusOne = [int(i) for i in str(integer)]
        return digitsPlusOne
    
obj = Solution()
array = obj.plusOne([9, 9])
print(array)