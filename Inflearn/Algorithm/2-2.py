T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print ("#%d %d" %(i+1, a[k-1]))

'''
인프런 파이썬 알고리즘 문제풀이, 2-2 K번째 수
문제 출처 : 한국정보올림피아드 문제
'''

