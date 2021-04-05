#define Max 50
typedef struct BtNode {
	int data;
	int size;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;

void Creattree(BiTree& T, int A[], int n, int len) {
	if (n >= len)
		T = NULL;
	else {
		T = (BiTree)malloc(sizeof(BtNode));
		T->data = A[n];
		Creattree(T->lchild, A, 2 * n + 1, len);
		Creattree(T->rchild, A, 2 * n + 2, len);
	}
}
//·ÇµÝ¹é
int Btdepth(BiTree T) {
	if (!T)
		return 0;
	int front = 0, rear = 0;
	int last = 1, level = 0;
	BiTree Q[Max];
	Q[rear++] = T;
	BiTree p;
	while (front < rear) {
		p = Q[front++];
		if (p->lchild)
			Q[rear++] = p->lchild;
		if (p->rchild)
			Q[rear++] = p->rchild;
		if (front == last) {
			level++;
			last = rear;
		}
	}
	return level;
}
//µÝ¹é
int Btdepth2(BiTree T) {
	if (!T)
		return 0;
	int ldep = Btdepth2(T->lchild);
	int rdep = Btdepth2(T->rchild);
	if (ldep > rdep)
		return ldep + 1;
	else
		return rdep + 1;
}