#include<stdio.h>
#include "eg.h"
//eg4
double eg4(double a, double b)
{
	printf("Through the calculate,the result is %lf.", 1 / ((1 / a + 1 / b) / 2));
	return 0;
}


//eg1
double min(double a, double b)
{
	if (a > b)
		return b;
	else
		return a;
}
void getnumber(double* x, double* y)
{
	double a, b;
	printf("Please input two numbers:\n");
	while ((scanf_s("%lf %lf", &a, &b)) != 2)
	{
		scanf_s("%*s");
		printf("Please enter two float.\n");
	}
	*x = a; *y = b;
}