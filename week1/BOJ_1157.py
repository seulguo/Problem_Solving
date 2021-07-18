import sys
a = input().lower()
b = list(set(a)) #중복제거 
c = list()

max = 0

for i in b: #중복을 제거하고 남아있는 글자에 대해
    if max <= a.count(i): #중복을 제거하기 전 단어에서 카운트 
        max = a.count(i) #max를 찾고 
        c.append(max) #새로운 list에 추가 
        temp = i #값 (알파벳 저장 )

c.sort(reverse=True) #내림차 순으로 정렬

if c.count(max) >= 2: #max를 카운트 했을 때 2 이상이면 중복 
    print("?")
else :
    print(temp.upper())

'''
2-5 단어공부
https://www.acmicpc.net/problem/1157
'''