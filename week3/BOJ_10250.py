T = int(input())
ans = list()

for i in range(T):
    H, W, n = map(int, input().split())
    floor = n % H 
    number = (n // H) + 1 

    if floor == 0:
        floor = H
        number -= 1

    if number < 10 : 
        number = "0" + str(number)
    ans.append(str(floor) + str(number)) 

for i in ans:
    print(i)

'''
12-10 ACM 호텔 
https://www.acmicpc.net/problem/10250
'''