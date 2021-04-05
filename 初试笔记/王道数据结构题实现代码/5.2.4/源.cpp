#include "head.h"
int main(void) {
	Agraph G;
	CreatGraph(G);
	int Arcs[5][5] = {};
	
	Convert(G, Arcs);
	for (int i = 0; i < Maxsize; i++) {
		for (int j = 0; j < Maxsize; j++)
			printf("%d ", Arcs[i][j]);
		printf("\n");
	}
	return 0;
}