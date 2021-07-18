'''
class Solution:
    def divisorGame(self, n: int) -> bool:
        x = list()
        cnt = 0 
        while n != 1:
            for i in range(1, n):
                if n % i == 0:
                    x.append(i) 
            n -= x[0]
            cnt += 1
        if cnt % 2 == 0:
            return False
        else: 
            return True
'''

'''
16-1 Divisor Game 
https://leetcode.com/problems/divisor-game/
'''