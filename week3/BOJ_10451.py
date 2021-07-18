import sys
sys.setrecursionlimit(10000)

n = int(input())
ans = list()

def dfs(start):
    visit[start] = 1
    next = a[start]
    if visit[next] == 0:
        dfs(next)


for i in range(n):
    num = int(input())
    a = [0] + list(map(int, input().split()))
    cycle = 0 
    visit = [1] + [0]*num

    for i in range(1, num+1):
        if(visit[i] == 0):
            dfs(i)
            cycle += 1 
    
    ans.append(cycle)

for i in ans:
    print(i)

'''
10451 순열 사이클
https://www.acmicpc.net/problem/10451
'''