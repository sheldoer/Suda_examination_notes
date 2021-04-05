#include "head.h"
/*
算法思想:利用先序遍历递归访问每一个节点，找到值为x的节点进行删除子树操作，删除子树是根据后序遍历以x为根的子树，逐点删除。
*/
int main(void) {
	int num[Max];
	for (int i = 0; i < Max; i++)
		num[i] = i+1;
	BiTree T;
	Creattree(T, num, 0, Max);
	Preorder(T);
	printf("\n");
	PreX(T, 3);
	Preorder(T);
	return 0;
}