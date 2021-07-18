n = int(input())
a = list(map(int, input().split()))
a.sort()

tmp = 0
ans = 0
for i in a:
     tmp += i 
     ans += tmp

print(ans)

'''
17-9 ATM 
https://www.acmicpc.net/problem/11399
'''