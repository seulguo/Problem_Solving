'''
3kg / 5kg
'''
n = int(input())
ans = 0
while True:
    if n % 5 == 0: #5kg짜리를 많이 사용하도록
        ans += (n//5) 
        print(ans)
        break

    n -= 3 #3kg짜리를 적게 사용하도록 
    ans += 1

    if n < 0: #남는게 생기면 (0%5는 0이므로)
        print(-1)
        break

'''
9-10 설탕 배달
https://www.acmicpc.net/problem/2839
'''
