from typing import List

def bestTime(nums: List[int]) -> int: # 0(n^2)
    max_profit = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            max_profit = max(max_profit, j - i)

    return max_profit

def bestTimeOnePass(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit



max_profit = bestTime([7,1,5,3,6,4])
print(max_profit)

max_profit2 = bestTimeOnePass([7,1,5,3,6,4])
print(max_profit2)
            
