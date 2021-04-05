#include<stdio.h>
#include<stdlib.h>
typedef struct BtNode {
	char data;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;
void Preorder(BiTree T,int n,int k) {
	if (T != NULL)
	{
		if (n == k)
			printf("%d ", T->data);
		else
			n++;
		Preorder(T->lchild,n,k);
		Preorder(T->rchild,n,k);
	}
}
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