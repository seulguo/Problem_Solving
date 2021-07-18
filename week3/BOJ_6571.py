ans = list()

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0 : break
    
    x, y, cnt = 0, 1, 0 
    while y <= b:
        x, y = y, (x+y)
        if y>=a and y<=b : 
            cnt += 1
    
    ans.append(cnt)

for i in ans:
    print(i)

'''
4-10 피보나치 수의 개수 
https://www.acmicpc.net/problem/6571
'''