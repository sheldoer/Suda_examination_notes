#include<stdio.h>
#include<stdlib.h>
typedef struct BtNode {
	char data;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;
BiTree Preincreat(char A[], char B[], int l1, int h1, int l2, int h2) {
	BiTree root = (BiTree)malloc(sizeof(BtNode));
	root->data = A[l1];
	int i = l2;
	for (; B[i] != root->data; i++);
	int llen = i - l2;
	int rlen = h2 - i;
	if (llen)
		root->lchild = Preincreat(A, B, l1 + 1, l1 + llen, l2, l2 + llen - 1);
	else
		root->lchild = NULL;
	if (rlen)
		root->rchild = Preincreat(A, B, h1 - rlen + 1, h1, h2 - rlen + 1, h2);
	else
		root->rchild = NULL;
	return root;
}
void Creat(char A[], char B[], BiTree& T, int al, int ah, int bl, int bh) {
	if (al <= ah&&al<=5&&al>=0)
	{
		T = (BiTree)malloc(sizeof(BtNode));
		T->data = A[al];
		int i = bl;
		while (i <= bh) {
			if (B[i] == T->data)
				break;
			i++;
		}
		Creat(A, B, T->lchild, al + 1, al + i - bl, bl, i - 1);
		Creat(A, B, T->rchild, al-bl + i + 1, ah, i+1, bh);
	}
	else
		T = NULL;
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
//preorder
void Preorder(BiTree T) {
	if (T != NULL)
	{
		printf("%c ", T->data);
		Preorder(T->lchild);
		Preorder(T->rchild);
	}
}
void Inorder(BiTree T) {
	if (T != NULL)
	{
		Inorder(T->lchild);
		printf("%c ", T->data);
		Inorder(T->rchild);
	}
}