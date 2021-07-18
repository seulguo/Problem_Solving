from collections import deque
dq = deque()
n, k = map(int, input().split())
ans = list()

for i in range(n):
    dq.append(i+1)

while len(dq)>0:
    for i in range(k):
        tmp = dq.popleft()
        dq.append(tmp)
    ans.append(dq.pop())

answer = ", ".join(map(str, ans))
print("<"+answer+">")

'''
6-2 요세푸스 문제 0 
https://www.acmicpc.net/problem/11866
'''
