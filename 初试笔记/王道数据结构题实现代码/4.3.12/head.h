#include<stdio.h>
#include<stdlib.h>
#define Max 20

typedef struct BtNode {
	int data;
	int size;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;
void Creattree(BiTree& T, int A[], int n, int len) {
	if (n >= len)
		T = NULL;
	else {
		T = (BiTree)malloc(sizeof(BtNode));
		T->data = A[n];
		Creattree(T->lchild, A, 2 * n + 1, len);
		Creattree(T->rchild, A, 2 * n + 2, len);
	}
}
int Print_xparents(BiTree T,int x) {
	if (T) 
		if (Print_xparents(T->lchild,x) || Print_xparents(T->rchild,x)|| T->data == x)
			{
				printf("%d ", T->data);
				return 1;
		}
	return 0;
}