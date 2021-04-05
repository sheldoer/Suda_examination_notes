#include"head.h"
/*
算法思想：采用非递归的层次遍历，把每一层的叶子节点进行加权求和；
*/
int main(void) {
	//建立二叉树
	int num[Max];
	for (int i = 0; i < Max; i++)
		num[i] = i + 1;
	BiTree T;
	Creattree(T, num, 0, Max);

	printf("%d ", wpl(T));
	return 0;
}