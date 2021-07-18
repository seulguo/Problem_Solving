'''
preorder = 루트 왼쪽 오른쪽
postorder = 왼쪽 루트 오른쪽
'''
import sys
sys.setrecursionlimit(10 ** 9)

pre = list()
post = list()

while True:
    try:
        pre.append(int(input()))
    except:
        break

def pre_to_post(left, right):
    if left > right:
        return 
    
    div = right + 1  
    for i in range(left+1, right+1): #루트 제외
        if pre[left] < pre[i]: #루트보다 크면 
            div = i #그 다음 분기점 
            break

    pre_to_post(left+1, div-1)
    pre_to_post(div, right)
    post.append(pre[left])

pre_to_post(0, len(pre)-1)
print("\n".join(map(str,post)))

'''
9-1 이진 검색 트리 
https://www.acmicpc.net/problem/5639
'''