import sys
n = int(sys.stdin.readline().rstrip())
ans = list()

for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    ans.append(a+b)

for i in ans:
    print(i)

'''
8-8 빠른 A+B
https://www.acmicpc.net/problem/15552
'''