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
int Ancestor(BiTree root, BiTree p, BiTree q, BiTree &r) {
	if (!root)
		return 0;
	if (Ancestor(root->lchild, p, q, r) || Ancestor(root->rchild, p, q, r))
	{
		r = root;
		return 0;
	}
	return root == p || root == q ? 1 : 0;
}