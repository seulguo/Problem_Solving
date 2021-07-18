'''
def solution(a, b):
    month = [31, 29, 31, 30 ,31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    sum = 0 
    if a>1: #1월이 아니면
        for i in range(a-1): #바로 직전 월까지 
            sum += month[i] #모든 날짜들을 더해서
    sum += b #현 월의 날짜까지 더해서 
    ans = sum % 7 #7로 나누었을 때 나머지에 따라 계산 
    
    return day[ans]
'''

'''
10-5 2016년
https://programmers.co.kr/learn/courses/30/lessons/12901

'''