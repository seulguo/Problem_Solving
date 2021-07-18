arr = list(map(int, input().split()))

asc = [1, 2, 3, 4, 5, 6, 7, 8]
dsc = [8, 7, 6, 5, 4, 3, 2, 1]

if(arr==asc):
    print("ascending")
elif(arr==dsc):
    print("descending")
else:
    print("mixed")

'''
1-1 음계 판별하기 백준 
https://www.acmicpc.net/problem/2920
'''