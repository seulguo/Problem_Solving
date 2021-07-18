n = int(input())
a = list()
ranking = list()

for i in range(n):
    w, h = map(int, input().split())
    a.append([w, h, i])

a.sort(key = lambda x: x[0])

cnt=0
for i in range(0, n):
    for j in range(i+1, n):
        if j == n+1 :
            break
        if a[i][0] < a[j][0] and a[i][1] < a[j][1] :
            cnt+=1
    ranking.append([cnt+1, a[i][2]])
    cnt = 0 

ranking.sort(key = lambda x : x[1])

for i in range(n):
    print(ranking[i][0], end=" ")

'''
20-8 덩치 
https://www.acmicpc.net/problem/7568
'''