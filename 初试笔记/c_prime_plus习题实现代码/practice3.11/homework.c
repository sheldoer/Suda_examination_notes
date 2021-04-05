#include<stdio.h>
int main(void)
{
	/*
	//eg2
	int ch;
	scanf_s("%d",&ch);
	printf("You have inputted a char,It is %c", ch);
	*/
	//eg5 transform ages to seconds
	int age;
	float second;
	scanf_s("%d", &age);
	second = age * 3.156e7;
	printf("You have live %le seconds", second);

	return 0;

}