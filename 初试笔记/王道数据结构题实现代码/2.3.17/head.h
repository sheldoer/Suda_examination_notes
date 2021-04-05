#include<stdio.h>
#include<stdlib.h>

typedef struct Dnode {
	int data;
	struct Dnode* prior, * next;
}Dnode, * Dlinklist;

bool Judgement(Dlinklist h) {
	Dnode* p = h->next;
	Dnode* q = p->prior;
	while (p != q && p->next != q) {
		if (p->data != q->data)
			return false;
		p = p->next;
		q = q->prior;
	}
	return true;
}