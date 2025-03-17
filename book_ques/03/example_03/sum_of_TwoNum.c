/*
program to calculate the sum of two numbers
*/


#include<stdio.h>

int main(){
  int num1,num2;
  printf("enter the first number :");
  scanf("%d",&num1);
  printf("enter the second number :");
  scanf("%d",&num2);
  int sum = num1 + num2;
  printf("sum of %d and %d : %d ",num1,num2,sum);
  return 0;
}
