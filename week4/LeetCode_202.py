'''
 class Solution:
    def isHappy(self, n: int) -> bool:
        
        while True:
            tmp = 0
            s = str(n)
            for i in s:
                tmp += int(i)*int(i)
            n = tmp 
            
            if n == 1:
                return True
            
            elif n == 2 or n == 4 or n == 6 or n == 8 :
                return False
        
'''

'''
16-6 Happy Number
https://leetcode.com/problems/happy-number/
'''