A, B = map(int, input().split())

A_100 = A//100
B_100 = B//100
A_1 = (A%100)%10
A_10 = (A%100) - A_1 
B_1 = (B%100)%10
B_10 = (B%100) - B_1

A = A_1*100 + A_10 + A_100
B = B_1*100 + B_10 + B_100

if A>B:
    print (A)
else: 
    print (B)

'''
BOJ_2908 상수 
https://www.acmicpc.net/problem/2908
'''