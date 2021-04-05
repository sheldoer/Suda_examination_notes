#include<stdio.h>
#include<stdlib.h>

typedef struct Lnode {
	int data;
	struct Lnode* next;
}Lnode, * Linklist;

void Sort(Linklist& l) {
	Lnode* p = l->next, * pre;
	Lnode* r = p->next;
	p->next = NULL;
	p = r;
	while (p)
	{
		r = p->next;
		pre = l;
		while (pre->next && pre->next->data < p->data)
			pre = pre->next;
		p->next = pre->next;
		pre->next = p;
		p = r;
	}
}
