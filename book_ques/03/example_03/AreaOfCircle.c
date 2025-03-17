/*program to calculate the area of a circle when the radius is given*/

#include<stdio.h>

int main(){
  float area,radius;
  const float pi = 3.14;
  printf("enter the the radius of the circle: ");
  scanf("%f",&radius);
  area = pi * radius * radius;
  printf("area of circle with radius %f : %f",radius,area);
  return 0;
}
