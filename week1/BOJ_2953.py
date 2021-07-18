ans = list()

sum = 0
for i in range(5):
    a = list(map(int, input().split()))
    for j in a:
        sum += j
    ans.append(sum) #각 줄의 합을 ans 리스트에 추가
    a.clear()
    sum = 0

tmp = ans.copy() 
tmp.sort(reverse=True) #max를 구하기 위해 
for i in ans:
    if i == tmp[0]:
        print(ans.index(i)+1, tmp[0])

'''
4-1 나는 요리사다
https://www.acmicpc.net/problem/2953
'''