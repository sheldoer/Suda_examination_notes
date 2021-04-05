#include"head.h"
int main(void) {
	int num[Max];
	int A[] = { 1,2,4,5,3,6,7 };
	printf("%d\n", sizeof(A) / sizeof(int));
	int B[Max];
	int x;
	for (int i = 0; i < Max; i++)
		num[i] = i + 1;
	SqQueue Q;
	InitQueue(Q);
	BiTree T;
	Creattree(T, num, 0, Max);
	Preorder(T,Q);
	while (!isempty(Q)) {
		DeQueue(Q, x);
		printf("%d ", x);
	}
	//PretoPost(A, 0, 6, B, 0, 6);
	//for (int i = 0; i < Max; i++)
		//printf("%d ", B[i]);

	return 0;
}