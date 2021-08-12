N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = set()
for i in range (0, N):
    for j in range (i+1, N):
        for k in range (j+1, N):
            ans.add(a[i]+a[j]+a[k])

ans = list(ans)
ans.sort(reverse=True)
print(ans[K-1])

'''
인프런 파이썬 알고리즘 문제풀이, 2-3 K번째 큰 수 
문제 출처 : 한국정보올림피아드 문제
'''