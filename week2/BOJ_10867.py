n = int(input())
a = list(map(int, input().split()))

a = list(set(a))
a.sort()

for i in a:
    print(i, end=" ")
print()

'''
6-5 중복 빼고 정렬하기 
https://www.acmicpc.net/problem/10867
'''