T = int(input())
a = list()
for i in range(T):
    num, string = input().split()
    for j in string:
        a.append(j*int(num))
    a.append("\n")
for i in a:
    print(i, end="")

'''
BOJ_2675 문자열 반복
https://www.acmicpc.net/problem/2675
'''