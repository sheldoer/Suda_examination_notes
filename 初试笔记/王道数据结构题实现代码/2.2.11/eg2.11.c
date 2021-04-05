#include<stdio.h>

int Find_middle(int s1[], int s2[], int L);
int M_search(int A[], int B[], int n);

int main(void)
{
	int s1[] = { 11,13,15,17,19 };
	int s2[] = { 2,4,6,8,20 };

	int length = sizeof(s1) / sizeof(int);
	int middle = M_search(s1, s2, length);
	//int middle=Find_middle(s1, s2, length);
	printf("The middle of two nums is %d.", middle);

	return 0;
}

//made by me
int Find_middle(int s1[], int s2[], int L)
{
	int i = 0, j = 0; //i 为s1序号，j为s2序号
	for (int n = 0; n < L - 1; n++)
		if (s1[i] > s2[j])
			j++;
		else
			i++;
	if (s1[i] < s2[j])
		return s1[i];
	else
		return s2[j];
}

//answer
int M_search(int A[], int B[], int n)
{
	int s1 = 0, d1 = n - 1, m1, s2 = 0, d2 = n - 1, m2;//分别表示序列A和B的首位数、末位数和中位数
	while (s1 != d1 || s2 != d2) {
		m1 = (s1 + d1) / 2;
		m2 = (s2 + d2) / 2;
		if (A[m1] == B[m2])
			return A[m1];
		if (A[m1] < B[m2]) {
			if ((s1 + d1) % 2 == 0) {
				s1 = m1;
				d2 = m2;
			}
			else {
				s1 = m1 + 1;
				d2 = m2;
			}
		}
		else {
			if ((s2 + d2) % 2 == 0) {
				d1 = m1;
				s2 = m2;
			}
			else {
				d1 = m1;
				s2 = m2 + 1;
			}
		}
	}
	return A[s1] < B[s2] ? A[s1] : B[s2];
}