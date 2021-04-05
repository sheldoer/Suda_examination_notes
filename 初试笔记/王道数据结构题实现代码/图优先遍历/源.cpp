#include "head.h"
int main(void) {
	Graph G;
	CreatGraph(G);
	Bfstraverse(G);
	printf("\n");
	Dfstraverse(G);
	return 0;
}