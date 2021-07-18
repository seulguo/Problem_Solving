'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        cnt = 0
        for i in t:
            if i == s[cnt]:
                cnt += 1 
                
                if cnt == len(s):
                    return True
        
        return False
'''

'''
15-5 Is Subsequence
https://leetcode.com/problems/is-subsequence/
'''