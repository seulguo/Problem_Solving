n = int(input())
a = list(map(int, input().split()))
ans = list()

for i in range(n):
    start = a[i]
    end = 0
    for j in range(i+1, n):
        if a[i] < a[j]: 
            end = a[j]
            a[i] = a[j]
        else:
            break
    if end > start:
        ans.append(end-start)
    else:
        ans.append(0)

ans.sort(reverse=True)

print(ans[0])

'''
15-8 오르막길 
https://www.acmicpc.net/problem/2846
'''