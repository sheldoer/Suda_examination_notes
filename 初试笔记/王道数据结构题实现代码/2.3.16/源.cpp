#include"head.h"
/*
算法思想：依次遍历两个链表，如果元素相同，则同时向后遍历，如若不同，则A继续遍历，B重返起点继续进行比较，
直至A或B其中一个为空，如果B访问完了，说明B为A的子序列；
*/
int main(void) {
	//建立单链表
	Lnode* A = (Linklist)malloc(sizeof(Lnode));
	Lnode* p = A;
	int num[] = { 5,1,-3,4,-8,6,7,-2 };
	int len = sizeof(num) / sizeof(int);
	for (int i = 0; i < len; i++)
	{
		Lnode* r = (Linklist)malloc(sizeof(Lnode));
		r->data = num[i];
		p->next = r;
		p = r;
	}
	p->next = NULL;
	Lnode* B = (Linklist)malloc(sizeof(Lnode));
	p = B;
	int num2[] = { 1,-3,4,-8,6,3};
	len = sizeof(num2) / sizeof(int);
	for (int i = 0; i < len; i++)
	{
		Lnode* r = (Linklist)malloc(sizeof(Lnode));
		r->data = num2[i];
		p->next = r;
		p = r;
	}
	p->next = NULL;
	printf("%5s ", Judgement(A, B) ? "yes" : "no");
	return 0;
}