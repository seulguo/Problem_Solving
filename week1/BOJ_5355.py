n = int(input())
ans = list() #정답을 한번에 출력하기 위해서 

for i in range(n):
    sign = list(map(str, input().split())) 
    tmp = 0
    for j in sign:
        if j == '@':
            tmp *= 3
        elif j == '%':
            tmp += 5
        elif j == '#':
            tmp -= 7
        else:
            tmp = float(j) #첫번째 값이 무조건 숫자이므로
    ans.append(tmp)
    sign.clear()

for i in ans:
    print(format(i, ".2f"))

'''
5-1 화성수학
https://www.acmicpc.net/problem/5355
'''
