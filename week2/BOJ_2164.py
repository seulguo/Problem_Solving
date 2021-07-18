from collections import deque

n = int(input())
ans = deque()

for i in range(1, n+1):
     ans.append(i)

while(len(ans)>1):
    ans.remove(ans[0])
    tmp = ans[0]
    ans.remove(ans[0])
    ans.append(tmp)

print(ans[0])

'''
6-1 카드2
https://www.acmicpc.net/problem/2164
'''