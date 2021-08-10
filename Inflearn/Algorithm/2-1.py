N, K = map(int, input().split())
a = list()
for i in range(N):
    if N % (i+1) == 0:
        a.append(i+1)
print(a[K-1])

'''
인프런 파이썬 알고리즘 문제풀이, 2-1 K번째 약수
출처 : 한국정보올림피아드 문제
'''