#include"head.h"
/*
算法思想：把所给单链表A进行拆分，遍历每两个元素，奇数位保留，偶数位尾插到新链表上，最后分化为两个目标单链表。
*/
int main(void) {
	Lnode* A = (Linklist)malloc(sizeof(Lnode));
	Lnode* p = A;
	int num[] = { 1,-3,4,-8,6,7 };
	int len = sizeof(num) / sizeof(int);
	for (int i = 0; i < len; i++)
	{
		Lnode* r = (Linklist)malloc(sizeof(Lnode));
		r->data = num[i];
		p->next = r;
		p = r;
	}
	p->next = NULL;
	Lnode* B = Seperate(A);
	Lnode* q = B->next;
	p = A->next;
	while (p) {
		printf("%d ", p->data);
		p = p->next;
	}
	printf("\n");
	while (q) {
		printf("%d ", q->data);
		q = q->next;
	}

	return 0;
}