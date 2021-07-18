a = input()

cnt = 0
for i in a:
    cnt += 1
    if cnt <= 10:
        print(i, end="")
    else: 
        print()
        print(i, end="")
        cnt = 1
print()

'''
3-2 열개씩 끊어 출력하기 
https://www.acmicpc.net/problem/11721
'''