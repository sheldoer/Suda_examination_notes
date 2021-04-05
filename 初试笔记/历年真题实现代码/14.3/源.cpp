#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#define Max 100
bool Isprime(int x);
//void m_sort(int a[], int len);

typedef struct Lnode {
	int data;
	struct Lnode* next;
}Lnode, * Linklist;

int main(void)
{
	int a[Max];
	int x;
	Linklist head = (Linklist)malloc(sizeof(Lnode));
	head->next = NULL;
	printf("Please input a number:\n");
	scanf_s("%d", &x);
	int i = 2, count = 0;
	while (i <= x) {
		if (Isprime(i) && x % i == 0) {
			a[count++] = i;
			x = x / i;
		}
		else
			i++;
	}
	printf("初次建成数组为\n");
	for (i = 0; i < count; i++)
	{
		printf("%d\n", a[i]);
	}
	int len = sizeof(a) / sizeof(int);
	printf("%d %d\n", count, len);
	/*
	m_sort(a,count);
	printf("二次建成数组为\n");
	for (i = 0; i < count; i++)
	{
		printf("%d\n", a[i]);
	}
	*/
	Lnode* p = head;
	for (i = 0; i < count; i++) {
		Lnode* q = (Linklist)malloc(sizeof(Lnode));
		q->data = a[i];
		q->next = p->next;
		p->next = q;
	}
	p = head->next;
	Lnode* r;
	printf("最终建成链表为\n");
	while (p) {
		printf("%d\n", p->data);
		r= p;
		p = r->next;
		free(r);
		
	}
	return 0;
}

bool Isprime(int x) {
	if (x <= 1)
		return false;
	for (int i = 2; i < sqrt(x); i++)
		if (x % i == 0)
			return false;
	return true;
}
/*
void m_sort(int a[], int len) {
	for (int i = 0; i < len; i++) {
		for(int j=0;j<len;j++)
			if (a[i] < a[j]) {
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
	}
}
*/