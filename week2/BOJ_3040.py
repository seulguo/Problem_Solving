a = [0]*9
find = False

for i in range(9):
    a[i] = int(input()) #우선 다 넣기 

for i in range(9):
    for j in range(i+1, 9):
        if sum(a) - a[i] - a[j] == 100: #전체 합에서 2개를 뺐을 떄 100이 되면
            a.remove(a[i]) #그 값을 제거 
            a.remove(a[j-1]) #위에서 하나 제거했으므로 index는 j가 아니라 j-1
            find = True
            break   
    if find == True:
        break

a.sort() #오름차순으로 정렬 

for i in a:
    print(i)

'''
8-9 백설 공주와 일곱 난쟁이 
https://www.acmicpc.net/problem/3040
'''