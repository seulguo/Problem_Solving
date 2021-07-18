'''
baby sukhwan tururu turu
very cute tururu turu
in bed tururu turu
baby sukhwan

1 2 3 4 
5 6 7 8 
9 10 11 12
13 14 

15 16 17 18
19 20 21 22
23 24 25 26 
27 28 

29 30 31 32
33 34 35 36 
37 38 39 40 
41 42

'''
n = int(input())

if n % 14 == 1 or n % 14 == 13:
    print("baby")
elif n % 14 == 2 or n % 14 == 0:
    print("sukhwan")
elif n % 14 == 5:
    print("very")
elif n % 14 == 6:
    print("cute")
elif n % 14 == 9:
    print("in")
elif n % 14 == 10:
    print("bed")
elif n % 14 == 3 or n % 14 == 7 or n % 14 == 11:
    if n//14 < 3:
        print("tururu" + "ru"*(n//14))
    else:
        print("tu+ru*%s" %((n//14)+2))
else:
    if n//14 < 4:
        print("turu" + "ru"*(n//14))
    else: 
        print("tu+ru*%s" %((n//14)+1))


'''
3-9 아기 석환 뚜루루 뚜루
https://www.acmicpc.net/problem/15947
'''
