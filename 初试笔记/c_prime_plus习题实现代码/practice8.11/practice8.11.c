#include<stdio.h>
int main(void)
{
	/*//eg1
	int count=0;
	int ch;

	while ((ch = getchar()) != EOF)
		count++;
	printf("This text include %d chars.\n", count);*/

	//eg2
	int ch;
	int count=1;
	while ((ch = getchar()) != EOF)
	{
		if (ch == '\n')
			printf("\\n|%d ",ch);
		else if( ch == '\t')
			printf("\\t|%d ",ch);
		else if(ch>=0&&ch<=' ')
			printf("^%c|%d ",ch+64,ch);
		else
			printf("%c|%d ", ch,ch);
		if (count++ % 10 == 0)
			printf("\n");
	}
	printf("\n");

	return 0;
}