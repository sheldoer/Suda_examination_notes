#include<stdio.h>
#include<stdlib.h>
#define Max 6

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
void Delete(BiTree& T) {
	if (T)
	{
		Delete(T->lchild);
		Delete(T->rchild);
		free(T);
		T = NULL;
	}
}
void Search(BiTree bt, int x) {
	
}
void PreX(BiTree& T,int x)
{
	if (T) {
		if (T->data == x)
			Delete(T);
		else {
			PreX(T->lchild, x);
			PreX(T->rchild, x);
		}
	}
}

void Preorder(BiTree T) {
	if (T != NULL)
	{
		printf("  %d", T->data);
		Preorder(T->lchild);
		Preorder(T->rchild);
	}
}
void Inorder(BiTree T) {
	if (T != NULL)
	{
		Inorder(T->lchild);
		printf("%d", T->data);
		Inorder(T->rchild);
	}
}