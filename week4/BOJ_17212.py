n = int(input())
dp = [1000001]*(n+1)
dp[0] = 0
coin = [7,5,2,1]

for i in range (1, n+1):
    for j in coin:
        if j <= i and dp[i-j]+1 < dp[i]:
            dp[i] = dp[i-j]+1
print(dp[n])

'''
18-2 달나라 토끼를 위한 구매대금 지불 도우미
https://www.acmicpc.net/problem/17212
'''