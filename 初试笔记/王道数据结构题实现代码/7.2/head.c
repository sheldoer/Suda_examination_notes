#include<stdio.h>
#include<stdlib.h>
void Insertsort(int A[], int n) {
	int i, j;
	for (i = 2; i <= n; i++) 
		if (A[i - 1] > A[i]) {
			A[0] = A[i];
			for (j = i - 1; A[j] >A[0]; j--)
				A[j + 1] = A[j];
			A[j + 1] = A[0];
	}
}
void Insertsort2(int A[], int n) {
	int i, j, low, high, mid;
	for (i = 2; i <= n; i++) {
		A[0] = A[i];
		low = 1; high = i - 1;
		while (low <= high) {
			mid = (low + high) / 2;
			if (A[mid] > A[0])
				high = mid - 1;
			else
				low = mid + 1;
		}
		for (j = i - 1; j >= high + 1; --j)
			A[j + 1] = A[j];
		A[high + 1] = A[0];
	}
	
}
void shellsort(int A[], int n) {
	int dk, i, j;
	for (dk = n / 2; dk >= 1; dk = dk / 2)
		for (i = dk + 1; i <= n; ++i)
			if (A[i] < A[i - dk]) {
				A[0] =A[i];
				for (j = i - dk; j > 0 && A[0] < A[j]; j -= dk)
					A[j + dk] = A[j];
				A[j + dk] = A[0];
			}
}