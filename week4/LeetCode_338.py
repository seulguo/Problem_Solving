'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = list()
        for i in range(n+1):
            num = bin(i)
            ans.append(str(num).count("1"))
        return ans
'''

'''
18-1 Counting Bits
https://leetcode.com/problems/counting-bits/
'''