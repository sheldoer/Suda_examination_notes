#include "head.h"
/*
算法思想：基于双向链表的特点，Locate函数先查找值为x的节点，对该节点先用p进行标记，再进行前后结点的链接。
之后寻找适当的插入位置，用q进行标记，标记的p节点插入到节点之后即可。
*/
int main(void) {
	Dnode* L = (Dlinklist)malloc(sizeof(Dnode));
	Dnode* p = L;
	int num[] = { 1,2,3,4 };
	int len = sizeof(num) / sizeof(int);
	for (int i = 0; i < len; i++)
	{
		Dnode* r = (Dlinklist)malloc(sizeof(Dnode));
		r->data = num[i];
		r->freq = 0;
		p->next = r;
		r->prior = p;
		p = r;
	}
	p->next = NULL;
	p = Locate(L, 2);
	p = Locate(L, 3);
	p = Locate(L, 4);
	p = L->next;
	while (p) {
		printf("%d ", p->data);
		p = p->next;
	}
	return 0;
}