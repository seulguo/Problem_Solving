string = input()

for i in range(97, 123):
    for j in string:
        if j == chr(i):
            print(string.index(j), end=" ")
            break
    else:
        print("%d" %(-1), end=" ")
    
'''
BOJ_10809 알파벳 찾기
https://www.acmicpc.net/problem/10809
'''