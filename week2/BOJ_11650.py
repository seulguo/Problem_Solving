n = int(input())
ans = list()

for i in range(n):
    ans.append(list(input().split()))

ans.sort(key= lambda x : (int(x[0]), int(x[1])))

for i in range(len(ans)):
    print(ans[i][0], ans[i][1])

'''
7-6 좌표 정렬하기 
https://www.acmicpc.net/problem/11650
'''