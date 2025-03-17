#include<stdio.h>

int main(){
  int n;
  printf("length of array :");
  scanf("%d",&n);
  char arr[n];
  for(int i =0;i<n;i++){
    printf("index %d : \n ",i);
    scanf(" %c",&arr[i]);
  }
  return 0;
}
