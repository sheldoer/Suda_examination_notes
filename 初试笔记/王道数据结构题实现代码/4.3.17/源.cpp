#include"head.h"
/*
算法思想：用递归进行判同，出现不一致则返回不相似的信息，没有返回不相似的信息则是相似；
*/
int main(void) {
	int num[Max1];
	for (int i = 0; i < Max1; i++)
		num[i] = i + 1;
	BiTree T1;
	Creattree(T1, num, 0, Max1);
	int num2[Max2];
	for (int i = 0; i < Max2; i++)
		num2[i] = i + 1;
	BiTree T2;
	Creattree(T2, num, 0, Max2);
	printf("%4s \n", semble(T1, T2) ? "yes" : "no");

	return 0;
}