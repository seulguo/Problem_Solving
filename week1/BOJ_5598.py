n = input() 
a = list()
for i in n:
    if i == 'A' or i == 'B' or i == 'C' :
        a.append(ord(i)+23) 
    else : 
        a.append(ord(i)-3)
for i in a:
    print(chr(i), end="")

print()

'''
3-3 카이사르 암호
https://www.acmicpc.net/problem/5598
'''