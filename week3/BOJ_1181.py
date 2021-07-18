n = int(input())
arr = list()

for i in range(n):
    arr.append(input())

arr = list(set(arr))

arr.sort(key = lambda x: (len(x),x))

print("\n".join(arr))

'''
14-7 단어 정렬 
https://www.acmicpc.net/problem/1181
'''