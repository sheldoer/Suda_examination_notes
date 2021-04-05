#include<stdio.h>
#include<stdlib.h>
#define Max 11
#define SMax 50
//二叉树结构体
typedef struct BtNode {
	int data;
	int size;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;

typedef struct {
	BiTree data[SMax];
	int top;
}Sqstack;

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

void Initstack(Sqstack& s) {
	s.top = -1;
}
bool Stackempty(Sqstack s) {
	if (s.top == -1)
		return true;
	else
		return false;
}
bool Push(Sqstack& s, BiTree x)
{
	if (s.top == SMax - 1)
		return false;
	s.data[++s.top] = x;
	return false;
}
bool Pop(Sqstack& s, BiTree& x)
{
	if (s.top == -1)
		return false;
	x = s.data[s.top--];
	return true;
}
bool Gettop(Sqstack s, BiTree x) {
	if (s.top == -1)
		return false;
	x = s.data[s.top];
	return true;
}
void Preorder(BiTree& T, BiTree& head) {
	Sqstack S;
	Initstack(S);
	BiTree p = T, q = head;
	while (p || !Stackempty(S)) {
		if (p) {
			if (!p->lchild && !p->rchild) {
				q->rchild = p;
				q = p;
			}
			Push(S, p);
			p = p->lchild;
		}
		else
		{
			Pop(S, p);
			if (p!= q)
				p = p->rchild;
			else
				p = NULL;
		}
	}
	q->lchild = NULL;
}