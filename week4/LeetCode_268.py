'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = set(range(0, len(nums)+1))
        nums = set(nums)
        ans = list(length - nums)
        return ans[0]
'''

'''
20-2 Missing Number
https://leetcode.com/problems/missing-number/
'''