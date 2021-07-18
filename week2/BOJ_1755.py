alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

a , b = map(int, input().split())
ans = list()

for i in range (a, b+1):
    if i < 10:
        now = alpha[i] #숫자를 알파벳으로 교체 
    else:
        now = alpha[i//10] + alpha[i%10] #숫자를 한자리씩 나눠서 알파벳으로 교체 후 합치기 
    ans.append((now,i))

ans.sort(key = lambda x: x[0]) #알파벳 순서에 따라 정렬 

for i in range (len(ans)):
    print(ans[i][1], end=" ")
    if (i+1) % 10 == 0:
        print()

print()

'''
7-2 숫자놀이 
https://www.acmicpc.net/problem/1755
'''
        