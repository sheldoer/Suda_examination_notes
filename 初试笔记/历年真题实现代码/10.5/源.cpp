#include<stdio.h>

#define LISTSIZE 8

void move1(int num[], int length);
void move2(int num[], int len);

int main(void)
{
	int num[] = { 2,9,4,6,7,8,3,2,5 };
	int len = sizeof(num) / sizeof(int);
	move1(num, len);
	for (int i = 0; i < len; i++)
		printf("The %d number is %d\n", i + 1, num[i]);
	printf("\n");
	move2(num, len);
	for (int i = 0; i < len; i++)
		printf("The %d number is %d\n", i+1,num[i]);

	return 0;
}

void move1(int num[],int length)
{
	int i = 0, j = 1, temp;
	while (1)
	{
		while (num[i] % 2 == 0)
			i += 2;
		while (num[j] % 2 == 1)
			j += 2;
		if (i > length || j >= length)
			break;
		else
		{
			temp = num[i];
			num[i] = num[j];
			num[j] = temp;
		}
	}
}
void move2(int num[], int len)
{
	int d = 0, s = 1, temp;
	for (int i = 0; i < len; i++)
	{
		if (num[i] % 2 == 0)
		{
			temp = num[d];
			num[d] = num[s];
			d += 2;
		}
		else
		{
			temp = num[s];
			num[s] = num[d];
			s += 2;
		}
		if (d > len || s > len)
			break;
	}
}