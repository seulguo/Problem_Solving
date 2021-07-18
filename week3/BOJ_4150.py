n = int(input())

def fibo (n):
    if n == 0 or n == 1:
        return 1
    a, b = 0, 1 
    for x in range(n-1):
       a, b = b, a+b
    return b 

print(fibo(n))

'''
12-6 피보나치 수 
https://www.acmicpc.net/problem/4150
'''