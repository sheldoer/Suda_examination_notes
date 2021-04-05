#include<stdio.h>
#include<stdlib.h>
#define Max 5
#define Maxsize 100
//二叉树结构体
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
int wpl(BiTree root) {
	BiTree A[Maxsize];
	int rear = -1, front = -1;  //记录头尾节点
	int level = 1;     //记录层数
	int w = 0;         //记录权值
	BtNode* p = root;
	A[++rear] = p;
	int last = rear;
	while (front < rear) {
		p = A[++front];
		if (!p->lchild && !p->rchild)
			w += p->data * level;
		if (p->lchild)
			A[++rear] = p->lchild;
		if (p->rchild)
			A[++rear] = p->rchild;
		if (front == last) {
			level++;
			last = rear;
		}
	}
	return w;
}
