#include<stdio.h>
#include<stdlib.h>
typedef struct LNode {
	int data;
	LNode* next;
}LNode, * Linklist;
/*习题介绍的头插法 尾指针不是NULL*/
void split1(Linklist L, Linklist& L1, Linklist& L2) {
	if (L)
	{
		LNode* p;
		if (L->data % 2 == 1)
		{
			p = L;
			L = L->next;
			p->next = L1;
			L1 = p;
		}
		else {
			p = L;
			L = L->next;
			p->next = L2;
			L2 = p;
		}
		split1(L, L1, L2);
	}
}
/*自己创造的尾插法 暂时正确*/
void split2(LNode* p, Linklist& e, Linklist& s)
{
	if (p == NULL) {
		e->next = NULL;
		s->next = NULL;
	}
	else {
		if (p->data % 2 == 0) {
			e->next = p;
			e = p;
		}
		else {
			s->next = p;
			s = p;
		}
		split2(p->next, e, s);
	}
}

int main(void) {
	Linklist L = (Linklist)malloc(sizeof(LNode));
	L->data = 5;
	LNode* h = L,*p,*L1,*L2,*q;
	/*建立待分裂的单链表*/
	for (int i = 0; i < 5; i++)
	{
		Linklist p = (Linklist)malloc(sizeof(LNode));
		p->data = i;
		L->next = p;
		L = L->next;
	}
	if (L->next == NULL)
		printf("yes\n");
	L->next = NULL;
	/*分裂1与2*/
	//split1(h, L1, L2);
	L1= (Linklist)malloc(sizeof(LNode));
	L2=(Linklist)malloc(sizeof(LNode));
	LNode* e = L1, * s = L2;
	split2(h, e, s);
	/*检验程序 打印分裂的L1与L2成员*/
	q = L1->next;
	while (q!=NULL) {
		printf("L1 num is %d\n", q->data);
		L = q;
		q = q->next;
		free(L);
	}
	q = L2->next;
	while (q != NULL) {
		printf("L2 num is %d\n", q->data);
		L = q;
		q = q->next;
		free(L);
	}
	return 0;
}

