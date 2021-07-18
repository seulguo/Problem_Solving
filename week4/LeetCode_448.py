'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = set(range(1, len(nums)+1))
        nums = set(nums)
        return length-nums
'''

'''
16-2 Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''