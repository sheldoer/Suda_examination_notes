#include<stdio.h>
#include<stdlib.h>

typedef struct Lnode {
	int data;
	struct Lnode* next;
}Lnode, * Linklist;

void Adjustlist(Linklist& l) {
	Lnode* p = l->next;
	while (p && p->data <= 0)
		p = p->next;
	while (p->next) {
		if (p->next->data < 0) {
			Lnode* q = p->next;
			p->next = q->next;
			q->next = l->next;
			l->next = q;
		}
		else
			p = p->next;
	}
}
/*answer*/
void Adjustlist2(Linklist& l)
{
	Lnode* p = l;
	Lnode* s = l;
	Lnode* q;
	while (p->next){
		q = p->next;
		if (q->data < 0) {
			p->next = q->next;
			q->next = l->next;
			l->next = q;
			if (s == l)
				s = q;
		}
		else if (q->data == 0) {
			p->next = q->next;
			q->next = s->next;
			s->next = q;
		}
		else
			p = p->next;
	}
}

int main(void) {
	Lnode* L = (Linklist)malloc(sizeof(Lnode));
	Lnode* p = L;
	int num[] = { 1,-3,4,-8,6,7,-2};
	int len = sizeof(num) / sizeof(int);
	for (int i = 0; i < len; i++)
	{
		Lnode* r = (Linklist)malloc(sizeof(Lnode));
		r->data = num[i];
		p->next = r;
		p = r;
	}
	p->next = NULL;
	p = L->next;
	while (p) {
		printf("%d\n", p->data);
		p = p->next;
	}
	printf("----------\n");
	//Adjustlist(L);
	Adjustlist2(L);
	p = L->next;
	while (p) {
		printf("%d\n", p->data);
		p = p->next;
	}
	return 0;
}