#include<stdio.h>
#include<stdlib.h>

typedef struct Lnode {
	int data;
	struct Lnode* next;
}Lnode, * Linklist;

Lnode* Seperate(Linklist& A) {
	Linklist B = (Linklist)malloc(sizeof(Lnode));
	Lnode* p = A->next;
	Lnode* q = p->next, * r = B;
	while (p) {
		p->next = q->next;
		r->next = q;
		r = q;
		p = p->next;
		if (p&&p->next)
			q = p->next;
		else
			break;
	}
	r->next = NULL;
	return B;
}