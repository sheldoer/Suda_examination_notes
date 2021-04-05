#include"head.h"
/*
算法思想：利用队列对每一层进行遍历，计算每一层的节点数，把最大值存储起来，最后返回最大值。
*/
int main(void) {
	//建立二叉树
	int num[Max];
	for (int i = 0; i < Max; i++)
		num[i] = i + 1;
	BiTree T;
	Creattree(T, num, 0, Max);
	printf("%d ", Breath(T));
	return 0;
}