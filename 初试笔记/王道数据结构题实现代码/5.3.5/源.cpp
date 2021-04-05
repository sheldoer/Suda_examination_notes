#include"head.h"
int main(void) {
	for (int i = 0; i < Maxversize; ++i)
		visited[i] = false;
	int path[100];
	Graph G;
	CreatGraph(G);
	Findpath(G, 0,2, path, 0);
	return 0;
}