#include<stdio.h>
#include<stdlib.h>

typedef struct Lnode {
	int data;
	struct Lnode* next;
}Lnode, * Linklist;

void Print(Linklist& l) {
	Lnode* min, * p;
	while (l->next)
	{
		min = l;
		p = l->next;
		while (p->next) {
			if (p->next->data < min->next->data)
				min = p;
			p = p->next;
		}
		printf("%d ", min->next->data);
		p = min->next;
		min->next = p->next;
		free(p);
	}
}