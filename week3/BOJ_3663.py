n = int(input())
ans = list()

for i in range(n):
    a = list(input().strip())
    dis = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in a]
    pos = 0
    cnt = 0

    while True:
        cnt += dis[pos]
        dis[pos] = 0 

        if sum(dis) == 0 : 
            break

        left = 1
        right = 1

        while dis[pos - left] == 0:
            left += 1
        
        while dis[pos + right] == 0:
            right += 1
        
        if left < right:
            pos -= left
            cnt += left 
        
        else: 
            pos += right 
            cnt += right 
    ans.append(cnt)

for i in ans:
    print(i)

'''
15-9 고득점
https://www.acmicpc.net/problem/3663
'''