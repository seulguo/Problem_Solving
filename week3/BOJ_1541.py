a = input().split("-")
sum = 0 
for i in a[0].split("+"):
    sum += int(i)
for i in a[1:]:
    for j in i.split("+"):
        sum -= int(j)
print(sum)

'''
13-2 잃어버린 괄호 
https://www.acmicpc.net/problem/1541
'''