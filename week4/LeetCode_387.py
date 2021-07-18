'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        tmp = list(set(s))
        ans = list()
        for i in tmp:
            if s.count(i) == 1:
                ans.append(i)

        for i in s:
            if i in ans:
                return s.index(i)
                
        return -1
'''

'''
20-5 First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
'''