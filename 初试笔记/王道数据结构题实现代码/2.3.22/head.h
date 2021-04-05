#include<stdio.h>
#include<stdlib.h>

typedef struct Lnode {
	char data;
	struct Lnode* next;
}Lnode, * Linklist;

int Listlen(Lnode* head) {
	int len = 0;
	while (head->next != NULL) {
		len++;
		head = head->next;
	}
	return len;
}
Linklist find(Linklist l1, Linklist l2) {
	return l1;
}

Linklist find2(Linklist l1, Linklist l2) {
	int m, n;
	Lnode* p, * q;
	m = Listlen(l1);
	n = Listlen(l2);
	for (p = l1; m > n; m--)
		p = p->next;
	for (q = l2; m < n; n--)
		q = q->next;
	while (p->next != NULL && p->next->data != q->next->data) {
		p = p->next;
		q = q->next;
	}
	return p->next;
}
