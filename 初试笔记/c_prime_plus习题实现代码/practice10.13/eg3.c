#include "headfile.h"
#define SIZE 3
int get_length(void);
int max(int *num);
int* creat_testnum(int size,int num);
int eg3(int num[]);

int max(int num[])
{
	printf("%d\n", *num);

	int *n = &num[0];
	int max = -1000;
	for (int i = 0; i < SIZE; i++)
	{
		if (*(n + i) > max)
			max = *(++n);
		/*if (num[i] > max)
			max = num[i];*/
	}
	return max;
}
int* creat_testnum(int size,int num[SIZE])
{
	int temp;

	for (int i = 0; i < SIZE; i++)
	{
		printf("Please input the %d number to the num.\n",i+1);
		scanf_s("%d", &temp);
		num[i] = temp;
		//scanf_s("%d",&num[i]);            //等价上两行
	}
	return num;
}
int eg3(int num[])
{
	//int size = get_length();

	creat_testnum(SIZE,num);
	//printf("%d\n", *(num+1));
	//printf("%d\n", *(num+1));
	int m = max(num);
	printf("The biggest number is %d.\n", m);

	return 0;
}