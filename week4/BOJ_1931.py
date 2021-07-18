n = int(input())
a = list()

for i in range(n):
    first, second = map(int, input().split())
    a.append([first, second])
    
a.sort(key = lambda x: (x[1], x[0]))

time = 0
cnt = 0
for i, j in a:
    if i >= time:
        cnt += 1
        time = j

print(cnt)

'''
18-7 회의실 배정 
https://www.acmicpc.net/problem/1931
'''