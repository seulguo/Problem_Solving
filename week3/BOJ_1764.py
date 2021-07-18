n, m = map(int, input().split())
arr = list()
ans = list()

for i in range(n+m):
    arr.append(input())
arr.append("")
arr.sort()


cnt=0
for i in range(n+m):
    if arr[i] == arr[i+1]:
        cnt+=1
        ans.append(arr[i])
        i+=2

print (cnt)
print ("\n".join(ans))

'''
15-10 듣보잡
https://www.acmicpc.net/problem/1764
'''
