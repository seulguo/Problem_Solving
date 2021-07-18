cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

a = input()

for i in cro:    
    a = a.replace(i, "!")

print(len(a))

'''
5-7 크로아티아 알파벳 
https://www.acmicpc.net/problem/2941
'''