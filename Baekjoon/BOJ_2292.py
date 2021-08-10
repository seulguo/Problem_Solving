N = int(input())
if N == 1 : 
    print (1)
else : 
    N -= 1
    cnt = 0
    while N > 0 :
        N = N - 6 * cnt
        cnt += 1
    print(cnt) 

'''
BOJ_2292 벌집 
https://www.acmicpc.net/problem/2292
'''