#include"head.h"
#define Max 7

int main(void) {
	char A[] = {'a','b','d','e','c','f'};
	char B[] = {'d','b','e','a','f','c'};
	//BiTree T=Preincreat(A,B,0,5,0,5);
	BiTree T;
	Creat(A, B, T, 0, 5, 0, 5);

	Preorder(T);
	printf("\n");
	Inorder(T);
	return 0;
}