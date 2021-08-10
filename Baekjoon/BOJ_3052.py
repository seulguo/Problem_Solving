ans = list()

for i in range(10):
    a = int(input())
    ans.append(a%42)

ans = set(ans)
print(len(ans)) 

'''
BOJ_3052 나머지 
https://www.acmicpc.net/problem/3052
'''