/*
문제 : 음계 
링크 : https://www.acmicpc.net/problem/2920
*/

#include <iostream>
using namespace std;

int main(){
  int arr[8];
  int asc = 0, dsc = 0;

  for(int i = 0; i<8; i++)
    cin >> arr[i];
  
  for(int i = 0; i<7; i++){
    if (arr[i] < arr[i+1])
      asc ++; 
    else 
      dsc ++;
  }

  if (asc == 7)
    cout << "ascending";
  else if (dsc == 7)
    cout << "descending";
  else 
    cout << "mixed";

  return 0; 
}