#include<stdio.h>
#include<stdlib.h>

typedef struct Lnode {
	int data;
	struct Lnode* next;
}Lnode, * Linklist;

void Deletsame(Linklist& l) {
	if (!l->next)
		return;
	Lnode* p = l->next;
	Lnode* q = p->next;
	while (q) {
		if (p->data == q->data)
		{
			p->next = q->next;
			free(q);
		}
		else
			p = q;
		q = p->next;
	}
}