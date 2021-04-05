#include<stdio.h>
#include<stdlib.h>
#define Max 7
#define Maxsize 50
//二叉树结构体
typedef struct BtNode {
	int data;
	int size;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;

typedef struct {
	int data[Maxsize];
	int front, rear;
}SqQueue;
void InitQueue(SqQueue& q){
	q.rear = q.front = 0;
}
bool EnQueue(SqQueue& q, int x) {
	if ((q.rear + 1) % Maxsize == q.front)return false;
	q.data[q.rear] = x;
	q.rear = (q.rear + 1) % Maxsize;
	return true;
}
bool DeQueue(SqQueue& q, int& x) {
	if (q.rear == q.front)return false;
	x = q.data[q.front];
	q.front = (q.front + 1) % Maxsize;
	return true;
}
bool isempty(SqQueue Q) {
	return Q.rear == Q.front ? true : false;
}
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
void PretoPost(int pre[], int l1, int h1, int post[], int l2, int h2) {
	int half;
	if (h1 >= l1) {
		post[h2] = pre[l1];
		half = (h1 - l1) / 2;
		PretoPost(pre, l1 + 1, l1 + half, post, l2, l2 + half - 1);
		PretoPost(pre, l1 + half + 1, h1, post, l2 + half, h2 - 1);
	}
}
void Preorder2(BiTree T) {
	if (T != NULL)
	{
		printf("  %d", T->data);
		Preorder2(T->lchild);
		Preorder2(T->rchild);
	}
}

void Preorder(BiTree T,SqQueue Q) {
	if (T != NULL)
	{
		EnQueue(Q, T->data);
		Preorder(T->lchild,Q);
		Preorder(T->rchild,Q);
	}
}
