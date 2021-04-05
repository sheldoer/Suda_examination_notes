#include<stdio.h>
#include<stdlib.h>
#define Maxsize 5
typedef struct {
	char Vex[Maxsize];
	int Edge[Maxsize][Maxsize];
	int vexnum, arcnum;
}Mgraph;

typedef struct Arcnode {
	int adjvex;
	struct Arcnode* next;
}Arcnode;
typedef struct Vnode{
	int data;
	Arcnode* first;
}Vnode, Adjlist[Maxsize];
typedef struct {
	Adjlist V;
	int vexnum, arcnum;
}Agraph;
/*
0->1
1->0->3
2->4
3->1
4->2
*/
void CreatGraph(Agraph& G) {
	for (int i = 0; i < Maxsize; i++) {
		G.V[i].data=i;
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
	G.V[2].first= p;
	p->next = NULL;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 1;
	G.V[3].first = p;
	p->next = NULL;
	p = (Arcnode*)malloc(sizeof(Arcnode));
	p->adjvex = 2;
	G.V[4].first = p;
	p->next = NULL;
}
void Convert(Agraph& G, int arcs[Maxsize][Maxsize]) {
	for (int i = 0; i < Maxsize; i++) {
		Arcnode* p = G.V[i].first;
		while (p) {
			arcs[i][p->adjvex] = 1;
			p = p->next;
		}//while
	}//for
}