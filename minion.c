#include<stdio.h>

int main()
{
    int N,X,ex,nm;
    scanf("%d %d",&N,&X);
    nm = (N*350);
    if(nm>X)
    {
        ex = nm-X;
    }
    else{
        ex = 0;
    }
    printf("%d",ex);
}