from collections import deque

n = int(input()) #단어 개수 

cnt = 0 #정답 
for i in range(n):
    a = input() #단어 
    b = list(set(a)) #단어에서 중복글자 제거

    tmp = deque() #중복을 제거한 (tmp 용)
    dq = deque() #단어 큐 
    for j in b:     
        tmp.append(j)
    for k in a:
        dq.append(k)

    first = dq.popleft()
    tmp.remove(first)
    
    tf = True
    while dq:
        second = dq.popleft()
        if first != second: #전과 후가 다를 때 
            if tmp.__contains__(second): #tmp큐에 포함돼 있으면 
                tmp.remove(second) #통과      
            else: #아니면 탈락 
                tf = False
        first=second
    
    if tf :
        cnt+=1

    tmp.clear()
    dq.clear()

print(cnt)

'''
2-6 그룹 단어 체커 
https://www.acmicpc.net/problem/1316
'''
