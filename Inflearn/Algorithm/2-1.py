N, K = map(int, input().split())
cnt = 0 
for i in range(N):
    if N % (i+1) == 0:
        cnt += 1 
    if cnt == K:
        print(i+1)
        break
else: 
    print(-1)

'''
인프런 파이썬 알고리즘 문제풀이, 2-1 K번째 약수
문제 출처 : 한국정보올림피아드 문제
'''