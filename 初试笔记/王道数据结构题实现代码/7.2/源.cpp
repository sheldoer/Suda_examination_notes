#include"head.c"
int main(void) {
	int num[] = { 0,3,5,2,7,4 };
	int len = sizeof(num) / sizeof(int);
	//Insertsort(num, len - 1);
	//Insertsort2(num, len-1);
	shellsort(num, len - 1);
	for (int i = 1; i < len; i++)
		printf("%d ", num[i]);
	return 0;
}