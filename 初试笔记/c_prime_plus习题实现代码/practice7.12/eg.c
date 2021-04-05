#include<stdio.h>
#include<ctype.h>
#include<stdbool.h>
#define STOP '#'
int main(void)
{
	/*eg1
	char ch,pre;
	long n_chars = 0L;
	int n_lines = 0, n_words = 0, p_lines = 0;
	bool inword = false;

	printf("Please enter text to analyzed(| to end):\n");
	pre = '\n';
	while ((ch = getchar()) !=STOP) 
	{
		n_chars++;   //Í³¼Æ×Ö·û
		if (ch == '\n')
			n_lines++;
		if (!isspace(ch) && !inword)
		{
			inword = true;
			n_words++;
		}
		if (isspace(ch) && inword)
			inword = false;
		pre = ch;
	}
	if (pre != '\n')
		p_lines = 1;
	printf("characters=%ld,words=%d,lines=%d,", n_chars, n_words, n_lines);
	printf("partial lines=%d\n", p_lines);
	*/
	
	/*//eg2 
	char ch;
	int i = 0;
	while ((ch = getchar()) != STOP)
	{
		printf("%d ", ch);
		if (i++ % 8 == 7)
			printf("\n");
	}*/

	/*//eg3
	int n,odd=0,even=0,osum=0,esum=0;
	printf("Please input a number to account(0 to quit):\n");
	while (scanf_s("%d", &n), n != 0) {
		n % 2 == 0 ? (even++,esum+=n) : (odd++,osum+=n);
	}	
	printf("You have put %d even numbers,and the average is %d ;\nYou have put %d odd numbers,and the average is %d .", 
		even, esum / even, odd, osum / odd);*/

	/*//eg 7
#define HOURSWAGE 1000
#define UPLIMIT 40
#define FIRSTSTAGE 300
#define FIRSTTAX 0.15
#define SECONDSTAGE 450
#define SECONDTAX 0.2
#define THIRDTAX 0.25
	int hours, salary, tax, recive;
	printf("Please input how many hours you have work:");
	scanf_s("%d", &hours);
	salary = hours <= UPLIMIT ? HOURSWAGE * hours : HOURSWAGE * UPLIMIT + 1.5*(hours - UPLIMIT);
	if (salary <= FIRSTSTAGE)
		tax = salary * FIRSTTAX;
	else if (salary <= SECONDSTAGE)
		tax = FIRSTSTAGE * FIRSTTAX + (salary - FIRSTSTAGE) * SECONDTAX;
	else
		tax = FIRSTSTAGE * FIRSTTAX + 150* SECONDTAX + (salary - SECONDSTAGE) * THIRDTAX;
	printf("Accoding to computer,your salary is %d,\nand you have paid taxs are %d,\nthen you have recived %d in your pocket."
		, salary, tax, salary - tax);*/

//eg11
#define seafood 2.05
#define beet 1.15
#define carrot 1.09
	float a=0,b=0,c=0,weight = 0, cost = 0, discount = 0, othercost = 0;
	char ch;
	printf("Welcome!\nwhat can I do for you? The price list is as follow:\nseafood:%5.2f;beet:%5.2f;carrot:%5.2f.\n", seafood, beet, carrot);
	printf("What's do you need?(q to quit)\n");
	while ((ch = getchar()) != 'q') {
		if ('\n' == ch)
			continue;
		switch (ch) {
		case'a':
			printf("How many seefood do you want:\n");
			scanf_s("%f", &a);
			break;
		case'b':
			printf("How many beet do you want:\n");
			scanf_s("%f", &b);
			break;
		case'c':
			printf("How many carrot do you want:\n");
			scanf_s("%f", &c);
			break;
		default:
			printf("Please reconsider.\n");
			break;
		}
		printf("What's more?(q to quit)\n");
	}
	weight = a + b + c;
	cost = seafood * a + beet * b + carrot * c;
	/*
	if (cost > 100) {
		cost = cost * 0.95;
		printf("congratulations,your have saved %.4f dollars.\n", cost * 0.05);
	}
	*/
	cost=cost<=100?cost:(printf("congratulations,your have saved %.4f dollars.\n", cost * 0.05),cost * 0.95);
	if (weight <= 5)
		othercost = 6.5;
	else if (weight <= 20)
		othercost = 14;
	else
		othercost = 14 + (weight - 20) * 0.5;
	printf("Then you have ordered %.2f pounds food;\nThe cost are %.2f ;\nand tranform have cost %.2f."
		, weight,cost,othercost);
/*//test
int i = 0;
i = 6<7? 3 : (4, 5);
printf("%d", i);*/

	return 0;
}