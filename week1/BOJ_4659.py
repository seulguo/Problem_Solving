from collections import deque

cnt=0
a = list()
b = list() 
vow = ['a', 'e', 'i', 'o', 'u']

pwd = input()
a.append(pwd)

def isVowel (x, password):
    if x in password:
        return True
    else:
        return False

while(pwd!="end"):
    pwd = input()
    a.append(pwd)
    b.append(pwd)

cnt = 0

for i in range(0, len(a)-1):

    for j in range (0,5):
        if(isVowel(vow[j], a[i])): #모음이 하나라도 포함 
            cnt += 1  
            break
    if(cnt == 0): #자음만 
        b[i] = "false"
    cnt = 0 
    ### ------ 1. 자음만 있으면 탈락 ------

    tmp = a[i]
    for k in range (0,5):
        if(isVowel(vow[k], a[i])):
            tmp = tmp.replace(vow[k], '!')  
    for l in tmp:
        if(l!='!'):
            tmp= tmp.replace(l,'@')
    if '!!!' in tmp:
        b[i] = "false"
    elif '@@@' in tmp:
        b[i] = "false" 
    ### ------ 2. 자음/모음 연속 3번은 탈락 ------

    dq = deque()
    for m in a[i]:
        dq.append(m)
    
    first = dq.popleft()

    for m in a[i]:
        if not dq:
            break
        second = dq.popleft()
        if(first == second and first != 'e' and first != 'o'):
            b[i] = "false"
        first = second
    ### ------ 3. 같은 문자가 2번이면 탈락 ------

for i in range (0, len(b)):
    if(b[i] == "false"):
        print("<{}> is not acceptable.".format(a[i]))
    else:
        print("<{}> is acceptable.".format(a[i]))

'''
2-1 비밀번호 발음하기
https://www.acmicpc.net/problem/4659
'''