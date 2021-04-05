#include"head.h"
int main(void) {
	Lnode* L1 = (Linklist)malloc(sizeof(Lnode));
	Lnode* p = L1;
	char num[] = { 'l','o','b','b','i','n','g' };
	int len = sizeof(num) / sizeof(char);
	for (int i = 0; i < len; i++)
	{
		Lnode* r = (Linklist)malloc(sizeof(Lnode));
		r->data = num[i];
		p->next = r;
		p = r;
	}
	p->next = NULL;
	Lnode* L2 = (Linklist)malloc(sizeof(Lnode));
	p = L2;
	char num2[] = { 'b','e','i','n','g' };
	len = sizeof(num2) / sizeof(char);
	for (int i = 0; i < len; i++)
	{
		Lnode* r = (Linklist)malloc(sizeof(Lnode));
		r->data = num2[i];
		p->next = r;
		p = r;
	}
	p->next = NULL;
	p = find2(L1, L2);
	while (p) {
		printf("%c ", p->data);
		p = p->next;
	}
	return 0;
}