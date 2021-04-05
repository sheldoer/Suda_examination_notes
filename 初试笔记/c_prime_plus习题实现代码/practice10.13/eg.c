#include "headfile.h"

int main(void)
{
	int num[3];
	eg3(num);

	return 0;
}
int get_length(void)
{
	int size;

	printf("What the length do you want?\n");
	scanf_s("%d", &size);

	return size;
}