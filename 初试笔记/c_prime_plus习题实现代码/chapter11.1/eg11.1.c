#include<stdio.h>
#define MSG "I am a symbolic string constant."
#define MAXLENGTH 81

int* test(int num[])
{
	
	int* p = num;
	return p;
}
void test2( int *p)
{
	printf("%d\n", *p);
	printf("%d\n", *(p++));
	printf("%d\n", *(++p));
}
int main(void)
{
	int num[] = { 1,5,3,4,5,6 };
	int* p = test(num);
	//printf("%p\n", *p);
	test2(p);

	return 0;
}