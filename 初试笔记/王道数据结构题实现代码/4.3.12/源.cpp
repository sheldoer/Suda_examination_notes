#include"head.h"

int main(void) {

	int num[Max];
	for (int i = 0; i < Max; i++)
		num[i] = i + 1;
	BiTree T;
	Creattree(T, num, 0, Max);

	Print_xparents(T, 18);
	return 0;
}