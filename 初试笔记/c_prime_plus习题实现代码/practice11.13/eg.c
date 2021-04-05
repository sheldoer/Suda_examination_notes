#include<stdio.h>
#include<string.h>
#define SIZE 80
char* eg1(char words[]);

int main(void)
{
	char words[SIZE];

	eg1(words);
	fputs(words, stdout);


	return 0;
}

char* s_gets(char* st, int n)
{
	char* ret_val;
	int i = 0;

	ret_val = fgets(st, n, stdin);
	if (ret_val)
	{
		while (st[i] != '\n' && st[i] != '\0')
			i++;
		if (st[i] == '\n')
			st[i] = '\0';
		else
			while (getchar() != '\n')
				continue;
	}

	return ret_val;
}
char* eg1(char words[])
{
	puts("Enter strings empty line to quit):");
	fgets(words, SIZE, stdin);

	return words;
}