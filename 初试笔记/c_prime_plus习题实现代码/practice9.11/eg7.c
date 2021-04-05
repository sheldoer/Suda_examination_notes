#include "eg.h"


int eg7(void)
{
	int ch;
	int a;
	while ((ch = getchar()) != EOF)
	{
		a = fun(ch);
		if (a == -1)
			printf("Input wrong,please try again.\n");
		else
			printf("%c is number %d.\n", ch, a);
		while ((ch=getchar())!= '\n')
			continue;
	}
	printf("Bye!\n");
	return 0;
}

int fun(char ch)
{
	int n;
	if (isalpha(ch))
	{
		ch = toupper(ch);
		n = ch - 64;
		return n;
	}
	else
		return -1;
}