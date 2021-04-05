#include "head.h"
/*
算法思想：因为是循环双链表，便可以通过头节点找到起始节点与末尾节点，
则从双链表两头同时遍历，查看元素是否对称，不对称则返回false，遍历完成未显示错误，则是对称的。
*/
int main(void) {
	Dnode* L = (Dlinklist)malloc(sizeof(Dnode));
	Dnode* p = L;
	int num[] = { 1,2,2,1};
	int len = sizeof(num) / sizeof(int);
	for (int i = 0; i < len; i++)
	{
		Dnode* r = (Dlinklist)malloc(sizeof(Dnode));
		r->data = num[i];
		p->next = r;
		r->prior = p;
		p = r;
	}
	p->next = L->next;
	p->next->prior = p;
	printf("%3s ", Judgement(L) ? "yes" : "no");
	return 0;
}