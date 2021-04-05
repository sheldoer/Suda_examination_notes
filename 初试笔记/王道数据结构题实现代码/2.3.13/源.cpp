#include"head.h"
int main(void) {
	Lnode* A = (Linklist)malloc(sizeof(Lnode));
	Lnode* p = A;
	int num[] = { 1,6,7,12 };
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
	int num2[] = { 2,4,7,9,15};
	len = sizeof(num2) / sizeof(int);
	for (int i = 0; i < len; i++)
	{
		Lnode* r = (Linklist)malloc(sizeof(Lnode));
		r->data = num2[i];
		p->next = r;
		p = r;
	}
	p->next = NULL;
	Linklist C = (Linklist)malloc(sizeof(Lnode));
	C=Incorperate(A, B);
	p = C->next;
	while (p) {
		printf("%d ", p->data);
		p = p->next;
	}
	return 0;
}