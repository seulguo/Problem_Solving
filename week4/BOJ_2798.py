n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = list()

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if (a[i] + a[j] + a[k]) <= m:
                ans.append([abs(m-(a[i] + a[j] + a[k])), (a[i] + a[j] + a[k])])

ans.sort(key = lambda x : x[0])

print(ans[0][1])

'''
20-6 블랙잭
https://www.acmicpc.net/problem/2798
'''

