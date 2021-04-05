#include "adt.h"

void del(LNode* & L, int x) {
	LNode* p;
	
	if (L == NULL)
		return;
	//printf("%p\n", L->next);
	if (L->data == x)
	{
		p = L;
		printf("%p\n", p);
		L = L->next;
		free(p);
		del(L, x);
	}
	else
		del(L->next, x);
}
void del2(Linklist& L, int x)
{
	LNode* p;
	printf("%d\n", L->next->data);
	if (L == NULL)
		return;
	if (L->data == x)
	{
		p = L;
		L = L->next;
		free(p);
		del2(L, x);
	}
	else if (L->next->data == x)
	{
		p = L->next;
		L->next = p->next;
		free(p);
		del2(L, x);
	}
	else
		del2(L->next,x);
}
/*收集并存储信息*/
LNode* CreateList(LNode* head) {
	int length, input;
	LNode* prev, * current;
	puts("Please input the length of the list:");
	scanf("%d", &length);
	prev = NULL;
	for (int i = 0; i < length; i++)
	{
		printf("Enter the %d number:\n", i + 1);
		scanf("%d", &input);
		current = (struct LNode*)malloc(sizeof(struct LNode));
		if (head == NULL)
			head = current;
		else
			prev->next = current;
		current->next = NULL;
		current->data = input;
		while (getchar() != '\n')
			continue;
		prev = current;
	}
	/*current = head;
	int j = 0;
	while (current != NULL)
	{
		printf("In the first list,the %d number is %d\n", ++j, current->data);
		//printf("%p\n", current);
		current = current->next;
	}*/
	return head;
}
/*显示列表*/
void ShowList(LNode*head) {
	LNode* current;
	if (head == NULL)
		printf("No data entered.");
	else
		printf("Here is the left list:\n");
	current = head;
	int j = 0;
	while (current != NULL)
	{
		printf("Through the function,the %d number is %d\n", ++j, current->data);
		//printf("%p\n", current);
		current = current->next;
	}
}
/*完成任务，释放已分配内存*/
void EmptyList(LNode* head) {
	LNode* current;
	current = head;
	while (head != NULL)
	{
		current = head;
		head = current->next;
		free(current);
	}
	printf("Bye!\n");
}