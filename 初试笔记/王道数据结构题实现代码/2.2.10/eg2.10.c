#include <stdio.h>

void Reverse(int R[], int from, int to)
{
	int i, temp;
	for (i = 0; i < (to - from+1) / 2; i++)
	{
		temp = R[from + i];
		R[from + i] = R[to - i];
		R[to - i] = temp;
	}
}

void Converse(int R[], int n, int p) {
	Reverse(R, 0, p - 1);
	Reverse(R, p, n - 1);
	Reverse(R, 0, n - 1);
}

int main(void) {
	int num[] = { 1,2,3,4,5,6,7,8 };
	for (int i = 0; i < 8; i++)
		printf("%d", num[i]);
	printf("\n");
	int length = sizeof(num) / sizeof(int),p;
	printf("What tap do you want to reverse?\n");
	scanf_s("%d", &p);
	Converse(num, length, p);
	for (int i = 0; i < 8; i++)
		printf("%d", num[i]);

	return 0;
}