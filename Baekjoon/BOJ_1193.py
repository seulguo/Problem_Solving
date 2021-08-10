N = int(input())
cnt = 1
while N > 0 : 
    N = N - cnt
    cnt += 1
    print(N)
print (cnt - 1) 
# 1, 2, 4, 7, 11, 16 
# a(n) = a(n-1) + n - 1 

# if N == 1 : 
#     print ("1/1")
# else : 
#     if (cnt - 1) % 2 != 0 :


# 1
# 2 3
# 4 5 6
# 7 8 9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 21 

# n = n + cnt
# N = N 
