n, v = map(int, input().split())
type_ = list()

for i in range(n):
    type_.append(int(input()))

type_.sort(reverse=True)

cnt = 0 
while v != 0 :
    for i in type_:
        if i <= v:
            v -= i 
            cnt += 1
            break

print(cnt)

'''
13-1 동전 0
https://www.acmicpc.net/problem/11047
'''