#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define Max 20
typedef struct BtNode {
	int data;
	int size;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;

int Givesize(BiTree& T);
void Creattree(BiTree& T, int A[], int n, int len);
void Preorder(BiTree T);
void Creatsize(BiTree T);
int NodeNum(BiTree T);

int main(void) {

	int num[Max];
	for (int i = 0; i < Max; i++)
	{
		num[i] = i;
	}
	BiTree T;
	//clock_t start, finish;
	//double  duration;
	Creattree(T, num, 0,Max);
	Creatsize(T);
	Preorder(T);
	printf("\n");
	//start = clock();
	Givesize(T);
	//finish = clock();
	Preorder(T);

	//duration = (double)(finish - start) / CLOCKS_PER_SEC;
	//printf("\n%f seconds\n", duration);
	return 0;
}
/*givesize*///failed
int Givesize(BiTree& T)
{
	if (T==NULL)
		return 0;
	else
	{
		return 1 + T->lchild->size + T->rchild->size;
		T->size=Givesize(T->lchild)+Givesize(T->rchild);
	}
	/*
	if (T->lchild)
	{
		T->size++;
		Givesize(T->lchild);
		T->size += T->lchild->size;
	}
	if (T->rchild)
	{
		T->size++;
		Givesize(T->rchild);
		T->size += T->rchild->size;
	}
	*/
}
/*creattree*/
void Creattree(BiTree& T, int A[], int n, int len) {
	if (n >=len)
		T = NULL;
	else {
		T = (BiTree)malloc(sizeof(BtNode));
		T->data = A[n];
		Creattree(T->lchild, A, 2 * n + 1, len);
		Creattree(T->rchild, A, 2 * n + 2, len);
	}
}
/*manifest tree*/
void Preorder(BiTree T) {
	if (T)
	{
		printf("%d %d ", T->data, T->size);
		Preorder(T->lchild);
		Preorder(T->rchild);
	}
}
/*answer*/
int NodeNum(BiTree T)
{
	if (T == NULL)
		return 0;
	else
		return 1 + NodeNum(T->lchild) + NodeNum(T->rchild);
}
void Creatsize(BiTree T)
{
	if (T == NULL)
		return;
	T->size = NodeNum(T);
	Creatsize(T->lchild);
	Creatsize(T->rchild);
	return;
}