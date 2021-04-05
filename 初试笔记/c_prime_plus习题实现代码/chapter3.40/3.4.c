#include<stdio.h>
int main(void) {
	unsigned int un = 3000000000;/*int is 32 bit,and short is 16 bit system.*/
	short end = 200;
	long big = 65537;
	long long verybig = 12345678908642;

	printf("un=%u and not %d\n",un,un);
	printf("end=%hd and %d\n", end, end);
	printf("big=%ld and not %hd\n", big, big);
	printf("verybig=%lld and not %ld\n", verybig, verybig);
	system("pause");
	printf("hi!\007\n");

	return 0;
}