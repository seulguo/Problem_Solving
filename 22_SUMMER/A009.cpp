/*
문제 : 문자열 다루기 기본   
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=cpp
*/

#include <string>
#include <iostream>

using namespace std;

bool solution(string s) {
    bool answer = true;
    if ((s.length() != 4 && s.length() != 6))
        return false;
        
    for(int i = 0; i < s.length(); i++){
        if(isdigit(s[i]) == false)
            answer = false;
    }
    
    return answer;
}