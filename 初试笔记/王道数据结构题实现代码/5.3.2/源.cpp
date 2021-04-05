#include"head.h"
int main(void) {
	Graph G;
	CreatGraph(G);
	int Arcs[Maxversize][Maxversize] = {};
	Convert(G, Arcs);
	for (int i = 0; i < Maxversize; i++) {
		for (int j = 0; j < Maxversize; j++)
			printf("%d ", Arcs[i][j]);
		printf("\n");
	}
	printf("%3s ", isTree(G) ? "yes" : "no");
	return 0;
}