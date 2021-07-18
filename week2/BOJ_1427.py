a = input()
ans = list()

for i in range(len(a)):
    ans.append(int(a[i]))

ans.sort(reverse=True)

for i in ans:
    print(i, end="")

'''
7-5 소트인사이드
https://www.acmicpc.net/problem/1427
'''