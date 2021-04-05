#include<stdio.h>
#include<stdlib.h>
#define Maxversize 5
#define Maxsize 100
typedef struct {
	int data[Maxsize];
	int front, rear;
}SqQueue;
void InitQueue(SqQueue& q) {
	q.rear = q.front = 0;
}
bool EnQueue(SqQueue& q, int x) {
	if ((q.rear + 1) % Maxsize == q.front)return false;
	q.data[q.rear] = x;
	q.rear = (q.rear + 1) % Maxsize;
	return true;
}
bool DeQueue(SqQueue& q, int& x) {
	if (q.rear == q.front)return false;
	x = q.data[q.front];
	q.front = (q.front + 1) % Maxsize;
	return true;
}
bool isempty(SqQueue Q) {
	return Q.rear == Q.front ? true : false;
}
typedef struct Arcnode {
	int adjvex;
	struct Arcnode* next;
}Arcnode;
typedef struct Vnode {
	 char data;
	Arcnode* first;
}Vnode, Adjlist[Maxversize];
typedef struct {
	Adjlist V;
	int vexnum, arcnum;
}Graph;
bool visited[Maxversize];
//深度优先遍历
void Dfs(Graph G, int v) {
	printf("%c ", G.V[v].data);
	visited[v] = true;
	for (Arcnode* w = G.V[v].first; w != NULL; w = w->next)
		if (!visited[w->adjvex])
			Dfs(G, w->adjvex);
}
void Dfstraverse(Graph G) {
	for (int v = 0; v < Maxversize; ++v)
		visited[v] = false;
	for (int v = 0; v < Maxversize; ++v)
		if (!visited[v])
			Dfs(G, v);
}
//广度优先遍历
void Bfs(Graph G, int v, SqQueue Q) {
	printf("%c ", G.V[v].data);
	visited[v] = true;
	EnQueue(Q, v);
	while (!isempty(Q)) {
		DeQueue(Q, v);
		for(Arcnode*w=G.V[v].first;w!=NULL;w=w->next)
			if (!visited[w->adjvex]) {
				printf("%c ", G.V[w->adjvex].data);
				visited[w->adjvex] = true;
				EnQueue(Q, w->adjvex);
			}//if
	}//while
}
void Bfstraverse(Graph G) {
	for (int i = 0; i < Maxversize; ++i)
		visited[i] = false;
	SqQueue Q;
	InitQueue(Q);
	for (int i = 0; i < Maxversize; ++i)
		if (!visited[i])
			Bfs(G, i,Q);

}
/*
0->1->4  a->b->e
1->0->3  b->a->d
2->4     c->e
3->1->4  d->b->e
4->0->2->3  e->a->b->c
*/
void CreatGraph(Graph& G) {
	for (int i = 0; i < Maxversize; i++) {
		G.V[i].data = 'a'+i;
		G.V[i].first = NULL;
	}
	Arcnode* p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 1;
	G.V[0].first = p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 4;
	G.V[0].first->next = p;
	p->next = NULL;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 0;
	G.V[1].first = p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 3;
	G.V[1].first->next = p;
	p->next = NULL;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 3;
	G.V[2].first = p;
	p->next = NULL;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 1;
	G.V[3].first = p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 4;
	G.V[3].first->next = p;
	p->next = NULL;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 0;
	G.V[4].first = p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 2;
	G.V[4].first->next = p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 3;
	G.V[4].first->next->next = p;
	p->next = NULL;
}