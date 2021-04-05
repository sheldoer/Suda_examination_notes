#include "head.h"
int main(void) {
	Graph G;
	CreatGraph(G);
	printf("%3s ", Bfstraverse(G, 1, 3) ? "yes" : "no");
	printf("\n");
	printf("%3s ", Dfstraverse(G, 1, 5) ? "yes" : "no");
	return 0;
}