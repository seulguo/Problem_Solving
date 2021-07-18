'''
from collections import deque

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = deque()
        odd = deque()
        for i in nums:
            if i % 2 == 0 :
                even.append(i)
            else: 
                odd.append(i)
        for i in range(0,len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()
        return nums
'''


'''
12-1 Sort Array By Parity 2
https://leetcode.com/problems/sort-array-by-parity-ii/
'''