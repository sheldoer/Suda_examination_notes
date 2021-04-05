#include<stdio.h>
#include<stdlib.h>
#define Maxversize 5
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
void Dfs(Graph G, int v, int& Vnum, int& Enum) {
	visited[v] = true;
	++Vnum;
	Arcnode* w = G.V[v].first;
	while (w) {
		Enum++;
		if(!visited[w->adjvex])
			Dfs(G, w->adjvex, Vnum, Enum);
		w = w->next;
	}
}
bool isTree(Graph& G)
{
	for (int i = 0; i < Maxversize; ++i)
		visited[i] = false;
	int Vnum = 0, Enum = 0;
	Dfs(G, 1, Vnum, Enum);
	if (Vnum == Maxversize && Enum == 2 * (Maxversize - 1))
		return true;
	else
		return false;
}
/*
0-1
1-0-3
2-4
3-1-4
4-2-3
*/
void CreatGraph(Graph& G) {
	for (int i = 0; i < Maxversize; i++) {
		G.V[i].data = 'a' + i;
		G.V[i].first = NULL;
	}
	Arcnode* p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 1;
	G.V[0].first = p;
	p->next = NULL;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 0;
	G.V[1].first = p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 3;
	G.V[1].first->next = p;
	p->next = NULL;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 4;
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
	p->adjvex = 2;
	G.V[4].first = p;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 3;
	G.V[4].first->next = p;
	p->next = NULL;
}
void Convert(Graph& G, int arcs[Maxversize][Maxversize]) {
	for (int i = 0; i < Maxversize; i++) {
		Arcnode* p = G.V[i].first;
		while (p) {
			arcs[i][p->adjvex] = 1;
			p = p->next;
		}//while
	}//for
}