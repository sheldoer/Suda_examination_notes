#include<stdio.h>
#include<stdlib.h>

typedef struct Lnode {
	int data;
	struct Lnode* next;
}Lnode, * Linklist;
void change(Linklist& l) {
	Lnode* h = l->next;
	l->next = NULL;
	Lnode*n = l;
	Lnode* q;
	while (h) {
		q = l->next;
		while (q) {
			if (q->data == h->data || q->data == -h->data)
				break;
			q = q->next;
		}
		if (!q) {
			n->next = h;
			h = h->next;
			n = n->next;
			n->next = NULL;
		}
		else
			h = h->next;
	}
}