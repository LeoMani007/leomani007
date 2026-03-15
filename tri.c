#include <stdio.h>
int main(){
	

	int c,i,j,k;
	printf("enter the number :");
	scanf("%d",&c);
	for(i=1;i<=c;i++){
		for(j=1;j<=c-i;j++){
			printf(" ");
			
		}
		for(k=1;k<=2*i-1;k++){
			printf("*");
		}
	printf("\n");
	}
return 0;
}
