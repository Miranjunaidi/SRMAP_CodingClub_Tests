


#include <stdio.h>

int fibSqrSum(int n){
  //This function should return the sum of the squares of the first n terms in the Fibonacci sequence

  //Write your code here

}



int main(){
  int NumTestCases, N;

  scanf("%d", &NumTestCases);
  for(int i = 0; i < NumTestCases; i++){
    scanf("%d", &N);
    printf("%d", fibSqrSum(N));
  }
  
  return 0;
}
