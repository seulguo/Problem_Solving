N = int(input())
cnt = 0
while N > cnt: 
    N = N - cnt
    cnt += 1

if cnt % 2 != 0 :
    print("%d/%d" %(cnt-N+1, N))
else : 
    print("%d/%d" %(N, cnt-N+1))

'''
BOJ_1193 분수찾기 
https://www.acmicpc.net/problem/1193
'''