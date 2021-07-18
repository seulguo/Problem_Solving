from collections import deque

n = int(input())
b = list() 

for i in range (n):
   a = list(input())
   dq = deque() #큐 생성
   for j in range (0, len(a)):
       dq.append(a[j]) #큐에 다 넣기 
   
   cnt = 0
   sum = 0

   first = dq.popleft() #하나를 빼서 first에 넣기 
   if(first == "O"): #first가 O면 sum++ 
       sum+=1 
 
   for j in range (0, len(a)+1):
        if not dq:
            break

        second = dq.popleft()

        if(first == second and first == "O"):
            cnt += 1
            sum += cnt
        else:
            cnt = 0
        #연속하면 cnt++, 그렇지 않으면 cnt=0 -> sum에 더해주기

        if(second == "O"):
            sum +=  1
        #second가 O면 sum++ 
        
        first = second
        
   b.append(sum)

for i in b:
       print(i)

'''
2-2 OX퀴즈
https://www.acmicpc.net/problem/8958
'''
