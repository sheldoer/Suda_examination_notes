#include"head.h"

int main(void) {
	Lnode* L = (Linklist)malloc(sizeof(Lnode));
	Lnode* p = L;
	int num[] = {7,10,10,21,30,42,42,51,70,70};
	int len = sizeof(num) / sizeof(int);
	for (int i = 0; i < len; i++)
	{
		Lnode* r = (Linklist)malloc(sizeof(Lnode));
		r->data = num[i];
		p->next = r;
		p = r;
	}
	p->next = NULL;

	Deletsame(L);
	p = L->next;
	while (p)
	{
		printf("%d ", p->data);
		p = p->next;
	}

	return 0;
}