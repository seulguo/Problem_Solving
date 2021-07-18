n = int(input())

a = list()
for i in range(n):
    a.append(list(input().split()))

a.sort(key = lambda x: int(x[0]))
for i in range(n):
    print(a[i][0], a[i][1])

'''
7-1 나이순 정렬
https://www.acmicpc.net/problem/10814
'''