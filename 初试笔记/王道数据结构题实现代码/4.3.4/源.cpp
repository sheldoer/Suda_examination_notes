#include<stdio.h>
#include<stdlib.h>
#include "head.h"
void levelorder(BiTree T,Sqstack&S) {
	if (T) {
		SqQueue Q;
		InitQueue(Q);
		BtNode* p = T;
		EnQueue(Q, p);
		while (!Isempty(Q)) {
			DeQueue(Q, p);
			Push(S, p);
			if (p->lchild)
				EnQueue(Q, p->lchild);
			if (p->rchild)
				EnQueue(Q, p->rchild);
		}
	}
}
int main(void) {
	int num[7];
	BtNode* p;
	Sqstack S;
	Initstack(S);
	for (int i = 0; i < 7; i++)
		num[i] = i;
	BiTree T;
	Creattree(T, num, 0, 7);
	levelorder(T, S);
	while (!Stackempty(S)) {
		Pop(S, p);
		printf("%d\n", p->data);
	}
	return 0;
}