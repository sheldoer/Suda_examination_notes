#include<stdio.h>
#include<stdlib.h>
#define Max1 5
#define Max2 9
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
int semble(BiTree T1, BiTree T2) {
	if (!T1 || !T2)
		return !T1 && !T2?1:0;
	return semble(T1->lchild, T2->lchild) && semble(T1->rchild, T2->rchild) ? 1 : 0;
}