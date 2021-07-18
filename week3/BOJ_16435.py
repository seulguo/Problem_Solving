'''
과일을 먹으면 길이가 1 늘어남 
자신의 길이보다 작거나 같은 높이의 과일만 먹을 수 윘음
최대 길이는? 
'''

N, L = map(int, input().split())
fruit = list(map(int, input().split()))

fruit.sort()
for i in fruit:
    if i > L:
        break
    else:
        L += 1

print(L)

'''
13-3 스네이크버드 
https://www.acmicpc.net/problem/16435
'''