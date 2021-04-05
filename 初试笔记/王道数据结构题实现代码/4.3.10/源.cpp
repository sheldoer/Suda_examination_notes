#define Max 8
#include"head.h"
int main(void) {
	int num[Max];
	for (int i = 1; i < Max; i++)
		num[i] = i;
	BiTree T;
	Creattree(T, num, 0, Max);
	Preorder(T, 0, 3);
	return 0;
}
