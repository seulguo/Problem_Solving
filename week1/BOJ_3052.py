a = list()

for i in range(10):
    n = int(input())
    a.append(n%42)

a = set(a) #set을 하면 중복이 제거 됨! 

print(len(a))

'''
4-3 나머지
https://www.acmicpc.net/problem/3052
'''