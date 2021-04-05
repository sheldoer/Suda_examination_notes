/*films1.c*/
#include<stdio.h>
#include<string.h>
#define TSIZE 45
//#define FMAX 5

struct film {
	char title[TSIZE];
	int rating;
};
char* s_gets(char str[], int lim);
int main(void)
{
	//struct film movies[FMAX];
	struct film* movies;
	int i = 0,n;
	int j;

	printf("Enter the maximum number of movies you'll enter:\n");
	scanf_s("%d", &n);
	while (getchar() != '\n')
		continue;
	movies = (struct film*)malloc(n * sizeof(struct film));
	puts("Enter first movies title:");
	while (i < n && s_gets(movies[i].title, TSIZE) != NULL && movies[i].title[0] != '\0')
	{
		puts("Enter your rating<0-10>:");
		scanf_s("%d", &movies[i++].rating);
		while (getchar() != '\n')
			continue;
		puts("Enter next movie title (empty line to stop):");
	}
	if (i == 0)
		printf("No data entered.");
	else
		printf("Here is the movie list:\n");

	for (j = 0; j < i; j++)
		printf("Movie:%s Rating:%d\n", movies[j].title, movies[j].rating);
	printf("Bye!\n");

	return 0;
}

char* s_gets(char* st, int n)
{
	char* ret_val;
	char* find;

	ret_val = fgets(st, n, stdin);
	if (ret_val)
	{
		find = strchr(st, '\n');
		if (find)
			*find = '\0';
		else
			while (getchar() != '\n')
				continue;
	}
	return ret_val;
}