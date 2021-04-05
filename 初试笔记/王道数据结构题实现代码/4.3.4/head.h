#define Max 50
typedef struct BtNode {
	int data;
	int size;
	struct BtNode* lchild, * rchild;
}BtNode, * BiTree;

typedef struct {
	BiTree data[Max];
	int front, rear;
}SqQueue;
void InitQueue(SqQueue& q)
{
	q.rear = q.front = 0;
}
bool Isempty(SqQueue q) {
	if (q.rear == q.front)return true;
	else return false;
}
bool EnQueue(SqQueue& q, BiTree x) {
	if ((q.rear + 1) % Max == q.front)return false;
	q.data[q.rear] = x;
	q.rear = (q.rear + 1) % Max;
	return true;
}
bool DeQueue(SqQueue& q, BiTree& x) {
	if (q.rear == q.front)return false;
	x = q.data[q.front];
	q.front = (q.front + 1) % Max;
	return true;
}
typedef struct {
	BiTree data[Max];
	int top;
}Sqstack;
void Initstack(Sqstack& s) {
	s.top = -1;
}
bool Stackempty(Sqstack s) {
	if (s.top == -1)
		return true;
	else
		return false;
}
bool Push(Sqstack& s, BiTree x)
{
	if (s.top == Max - 1)
		return false;
	s.data[++s.top] = x;
	return false;
}
bool Pop(Sqstack& s, BiTree& x)
{
	if (s.top == -1)
		return false;
	x = s.data[s.top--];
	return true;
}
bool Gettop(Sqstack s, BiTree x) {
	if (s.top == -1)
		return false;
	x = s.data[s.top];
	return true;
}

void Creattree(BiTree & T, int A[], int n, int len) {
	if (n >= len)
		T = NULL;
	else {
		T = (BiTree)malloc(sizeof(BtNode));
		T->data = A[n];
		Creattree(T->lchild, A, 2 * n + 1, len);
		Creattree(T->rchild, A, 2 * n + 2, len);
	}
}