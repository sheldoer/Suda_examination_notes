#include<stdio.h>
int main(void)
{
	/*//eg1 build a array
	char al[30];
	int j = 0;
	for (char i = 'a'; i <= 'z'; i++)
	{
		al[j++] = i;
		printf("%c",al[j-1]);
	}*/
	
	//eg4 nested loop
	char ch = 'A';
	int j = 0;
	while (ch != 'V') {
		j++;
		for (int i = 1; i <= j; i++)
		{
			printf("%c", ch++);
			if (ch == 'V')
				break;
		}
		printf("\n");
	}
	
}