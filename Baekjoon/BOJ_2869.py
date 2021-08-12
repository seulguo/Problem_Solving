A, B, V = map(int, input().split())

if (V-B)%(A-B) != 0:
    print ((V-B)//(A-B)+1)
else: 
    print ((V-B)//(A-B))

'''
BOJ_2869 달팽이는 올라가도 싶다 
https://www.acmicpc.net/problem/2869
'''