/*
문제 : 평균은 넘겠지  
링크 : https://www.acmicpc.net/problem/4344
*/

#include <iostream>
using namespace std;

int main(){
  int arr[1001];
  int max = 0;
  int N = 0;
  float sum = 0, avg = 0, count = 0;
  cin >> max;
  
  for(int i = 0; i<max; i++){
    cin >> N;
  
    sum = 0;
    for(int j = 0; j<N; j++){
      cin >> arr[j];
      sum += arr[j];
    }

    avg = 0;
    avg = sum / N; 

    count = 0;
    for(int j = 0; j<N; j++){
      if (arr[j] > avg)
        count ++;
    }

     cout<<fixed;
     cout.precision(3);
     cout << (count/N*100) << "%" << endl;
  }

  return 0; 
}

