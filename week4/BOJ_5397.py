from collections import deque
n = int(input())
ans = list()
for i in range(n):
    a = input()
    left = deque()
    right = deque()
    for j in a:
        if j == "<":
            if left:
                right.append(left.pop())
        elif j == ">":
            if right:
                left.append(right.pop())
        elif j == "-":
            if left:
                left.pop()
        else:
            left.append(j)
    left.extend(reversed(right))
    ans.append("".join(left))
    
for i in ans:
    print(i)

'''
20-10 키로거 
https://www.acmicpc.net/problem/5397
'''