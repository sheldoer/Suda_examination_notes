#include<stdio.h>

int Findmin(int A[], int len);

main()
{
	int A[] = { 1,2,-2,5,-6,8,-4,-3 };
	int len = sizeof(A) / sizeof(int);
	printf("%d\n", len);
	printf("The minest patch is %d\n", Findmin(A, len));
}
int Findmin(int A[], int len) {
	int min = 0;
	for (int i = 0; i < len; i++)
		if (A[i] < min)
			min = A[i];
	if (min >= 0)
		return 0;
	int sum = 0;
	for (int i = 0; i < len; i++)
	{
		sum += A[i];
		if (sum < min)
			min = sum;
		if (sum > 0)
			sum = 0;
	}
	return min;
}