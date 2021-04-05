#include "adt.h"


int main(void) {
	struct LNode* head = NULL;
	int x;

	head = CreateList(head);
	puts("What number dou you want to delete?");
	scanf("%d", &x);
	del(head,x);
	ShowList(head);
	EmptyList(head);

	return 0;
}


