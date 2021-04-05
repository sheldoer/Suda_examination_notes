#include<stdio.h>
main()
{
	int num[4] = { 4,6,9,11 };
	int* p = &num[0];
	for (int i = 0; i < 4; i++)
	{
		printf("%d\n", num[i]);
	}
	for (int i = 0; i < 4; i++)
	{
		printf("%d\n", *p);
		printf("%d\n", *p++);
	}
	return 1;
}