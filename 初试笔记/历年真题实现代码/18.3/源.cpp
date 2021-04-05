#include<stdio.h>
#include<stdlib.h>

typedef struct Lnode {
	int data;
	struct Lnode* next;
}Lnode, * Linklist;

bool Accordlist(Linklist L)
{
	Lnode* p = L -> next;
	while (p && p->data % 2 == 1) 
		p = p->next;
	while (p) {
		
		if (p->data % 2 ==1)
			return false;
		p = p->next;
	}
	return true;
}
/*answer*/
bool Iseven(Linklist head) {
	Lnode* p = head;
	if (p == NULL)
		return true;
	while (p)
	{
		if ((p->data) % 2 == 1)
			return false;
		p = p->next;
	}
	return true;
}
bool Isorder(Linklist head)
{
	Lnode* p = head->next;
	if (p == NULL)
		return true;
	while (p) {
		if ((p->data) % 2 == 0)
			return Iseven(p);
		p = p->next;
	}
	return true;
}

int main(void) {
	Lnode* L = (Linklist)malloc(sizeof(Lnode));
	Lnode* p = L;
	int num[] = { 1,3,4,8,6,7};
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
	if (Accordlist(L)==1)
		printf("·ûºÏ\n");
	else
		printf("false\n");

	if (Isorder(L))
		printf("yes\n");
	else
		printf("no\n");
	return 0;
}