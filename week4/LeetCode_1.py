'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = list()
        for i in range (0,len(nums)):
            for j in range (i+1, len(nums)+1):
                if j == len(nums) : break
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    
        return ans
'''

'''
16-5 Two Sum 
https://leetcode.com/problems/two-sum/
'''