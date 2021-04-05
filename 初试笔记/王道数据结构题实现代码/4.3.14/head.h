#include<stdio.h>
#include<stdlib.h>
#define Max 10
#define Maxsize 100
//二叉树结构体
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

int Breath(BiTree T) {
	if (!T)
		return 0;
	BiTree A[Maxsize];
	int front =-1, rear = -1;
	int breath = 0, b=0;
	BtNode *p;
	A[++rear] = T;
	int level = rear;
	while (front < rear) {
		p = A[++front];
		if (p->lchild)
			A[++rear] = p->lchild;
		if (p->rchild)
			A[++rear] = p->rchild;
		if (front == level) {
			if (++b > breath)
				breath = b;
			b = 0;
			level = rear;}
		else
			b++;
	}//while
	return breath;
}