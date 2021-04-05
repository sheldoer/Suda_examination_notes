#include"head.h"

int main(void) {
	int num[Max];
	for (int i = 1; i < Max; i++)
		num[i] = i;
	BiTree T;
	Creattree(T, num, 0, Max);
	printf("%d\n", Doublecount(T));

	return 0;

}