n = int(input())
a = input()
A = [0]*1000000 
B = [0]*1000000
#(1<= N <= 1,000,000) 이므로 

if a[0] == 'A':
    A[0] = 0 #A->A가 되려면 
    B[0] = 1 #A->B가 되려면 

else : 
    A[0] = 1 #B->A가 되려면 
    B[0] = 0 #B->B가 되려면 

for i in range(1, n): #a[1] - a[n-1]까지
    if a[i] == 'A':
        A[i] = min(A[i-1], B[i-1] + 1) # A->A : min(지금까지 A였던 count , 지금까지 B였던 count + 뒤집기) 
        B[i] = min(A[i-1] + 1, B[i-1] + 1) # A->B : min(지금까지 A였던 count + 뒤집기, 지금 까지 B였던 count + 1(A->B) )
    else :
        A[i] = min(A[i-1] + 1, B[i-1] + 1) # B->A : min(지금까지 A였던 count + 1(B->A), 지금까지 B였던 count + 뒤집기)
        B[i] = min(A[i-1] + 1, B[i-1]) # B->B : min(지금까지 A였던 count + 뒤집기, 지금까지 B였던 count)

print(A[n-1])

'''
13-5 DNA 발견
https://www.acmicpc.net/problem/2806
'''