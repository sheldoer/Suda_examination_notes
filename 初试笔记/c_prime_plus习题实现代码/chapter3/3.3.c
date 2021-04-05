#include<stdio.h>
int main(void) {
	int x = 100;

	printf("dec=%d;octa=%o;hex=%x\n", x, x, x);
	printf("dec=%d;octa=%#o;hex=%#x\n", x, x, x);

	return 0;
}