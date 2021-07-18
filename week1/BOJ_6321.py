n = int(input())
a = list()
b = list() 

for i in range(n):
    a.append(input())

cnt = 1
for i in a:
    for j in i:
        b.append(ord(j))
    
    print("String #{}".format(cnt))
    for k in b:
        if k==90:
            print(chr(65), end="")
        else:
            print(chr(k+1), end="")

    print()
    if cnt == len(a): 
        break  
    print()
    #출력형식.. 
    
    b.clear()
    cnt+=1

'''
1-8 IBM 빼기 1
https://www.acmicpc.net/problem/6321
'''
