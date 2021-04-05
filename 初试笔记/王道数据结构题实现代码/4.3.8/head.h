#include<stdio.h>
#include<stdlib.h>
#define Max 7
typedef struct BtNode {
	int data;
	int size;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;

void Creattree(BiTree & T, int A[], int n, int len) {
	if (n >= len)
		T = NULL;
	else {
		T = (BiTree)malloc(sizeof(BtNode));
		T->data = A[n];
		Creattree(T->lchild, A, 2 * n + 1, len);
		Creattree(T->rchild, A, 2 * n + 2, len);
	}
}
int Doublecount(BiTree T) {
	if (T == NULL)
		return 0;
	int lsize = Doublecount(T->lchild);
	int rsize = Doublecount(T->rchild);
	if (T->lchild && T->rchild)
		return 1 + lsize + rsize;
	else
		return lsize + rsize;
}