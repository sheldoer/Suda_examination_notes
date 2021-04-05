#include"head.h"
/*
算法思想：利用非递归遍历二叉树，将叶子节点尾插到头节点之后即可。
*/
int main(void) {
	//建立二叉树
	int num[Max];
	for (int i = 0; i < Max; i++)
		num[i] = i + 1;
	BiTree T;
	Creattree(T, num, 0, Max);
	BiTree L = (BiTree)malloc(sizeof(BtNode));
	Preorder(T, L);
	BiTree p = L->rchild;
	while (p) {
		printf("%d ", p->data);
		p=p->rchild;
	}
	return 0;
}