N = int(input())
a = list(map(int, input().split()))
max_num = max(a)
sum = 0 
for i in range(N):
    a[i] = a[i]/max_num*100 
    sum += a[i]
print(sum/N)

'''
BOJ_1546 평균 
https://www.acmicpc.net/problem/1546
'''