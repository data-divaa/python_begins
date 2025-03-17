#include<stdio.h>
#include<stdlib.h>

int main(){
  char num_string[50];
  printf("enter your string :");
  gets(num_string);
  int num ;
  num = atoi(num_string);
  printf("numeric string after conversion to integer is : ");
  puts(num);

  return 0;
}
