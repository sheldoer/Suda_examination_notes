#include<stdio.h>
#include<stdlib.h>

typedef struct Dnode {
	int data;
	int freq;
	struct Dnode* prior, * next;
}Dnode, * Dlinklist;
Dlinklist Locate(Dlinklist& l, int x) {
	Dnode* p = l->next, *q;
	while (p && p->data != x)
		p = p->next;
	if (!p)
		return NULL;
	p->freq++;
	q = p->prior;
	while (q != l && p->freq > q->freq)
		q = q->prior;
	p->prior->next = p->next;
	if (p->next != NULL) 
		p->next->prior = p->prior;
	p->next = q->next;
	p->next->prior = p;
	q->next = p;
	p->prior = q;
	return p;
}