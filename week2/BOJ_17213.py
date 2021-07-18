fruit = int(input()) 
num = int(input()) 

def combi(n, r):
    tmp1, tmp2 = 1, 1
    for i in range(r):
        tmp1 *= n
        tmp2 *= r
        n = n-1
        r = r-1
    return tmp1/tmp2

print(int(combi(num-1, num-fruit)))


'''
10-8 과일서리 
https://www.acmicpc.net/problem/17213
'''