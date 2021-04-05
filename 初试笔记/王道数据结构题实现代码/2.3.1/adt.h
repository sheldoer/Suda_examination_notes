#include<stdio.h>
#include<stdlib.h>

typedef struct LNode {
	int data;
	struct LNode* next;
}LNode, * Linklist;
void del(Linklist& L, int x);
LNode* CreateList(LNode* head);
void ShowList(LNode* head);
void EmptyList(LNode* head);
void del2(Linklist& L, int x);