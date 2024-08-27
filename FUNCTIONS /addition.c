#include <stdio.h>

int sum(int,int);

int sum(int x,int y){
printf("the sum is %d ",x+y);
return x+y;
}

int main() {
    int a=2;
    int b=4;
    int c=sum(a,b);
    printf("\n");
    int d=9;
    int o=10;
    int g=sum(d,o);
    
    return 0;
}
