#include<stdio.h>
#define MAXSIZE  100
/*mine*/
int AccordNum(int n)
{
	int temp = n;
	if (n % 2 == 0)
		n /= 2;
	if (n % 3 == 0)
		n /= 3;
	if (n % 5 == 0)
		n /= 5;
	if (n == 1)
		return 1;
	else if (n == temp)
		return 0;
	else
		return AccordNum(n);
}
/*answer*/
int Meet(int n)
{
	if (n == 1)
		return 1;
	else if (n % 2 == 0)
		return Meet(n / 2);
	else if (n % 3 == 0)
		return Meet(n / 3);
	else if (n % 5 == 0)
		return Meet(n / 5);
	else
		return 0;
}
//main 
 main()
 {
	int num1[MAXSIZE];
	int num2[MAXSIZE];
	int i = 0;
	int n = 1;
	while (i < MAXSIZE)
	{
		if (AccordNum(n))
			num1[i++] = n;
		n++;
	}
	int j = 0;
	n = 1;
	while (j < MAXSIZE)
	{
		if (Meet(n))
			num2[j++] = n;
		n++;
	}
	for (i = 0; i < MAXSIZE; i++)
		printf("%d %d\n", num1[i],num2[i]);
	
	return 0;
}