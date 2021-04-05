#include<stdio.h>
int main(void)
{
	int dogs;

	printf("How many dogs do you have?\n");
	scanf_s("%d", &dogs);
	printf("So you have %d dog(s)!\n", dogs);

	return 0;
}