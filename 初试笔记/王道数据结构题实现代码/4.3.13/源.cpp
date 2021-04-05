#include"head.h"
int main(void) {

	int num[Max];
	for (int i = 0; i < Max; i++)
		num[i] = i + 1;
	BiTree T;
	Creattree(T, num, 0, Max);
	BiTree p = T->lchild->lchild->lchild;
	BiTree q = T->lchild->lchild->rchild->lchild;
	BtNode* r = NULL;
	Ancestor(T, p, q, r);
	printf("%d ", r->data);

	return 0;
}