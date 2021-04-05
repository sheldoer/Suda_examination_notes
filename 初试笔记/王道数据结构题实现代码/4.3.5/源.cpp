#include<stdio.h>
#include<stdlib.h>
#include "head.h"
#define len 7
int main(void) {
	int num[len];
	BtNode* p;
	for (int i = 0; i < len; i++)
		num[i] = i;
	BiTree T;
	Creattree(T, num, 0, len);
	int h=Btdepth(T);
	return h;
}