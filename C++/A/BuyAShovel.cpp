#include <iostream>
#include <stdlib.h> 
using namespace std;
 
int main()
{
    long long int x;
    long long int y;
    cin>>x>>y;
    int i=1;
    while (((x*i)%10) != 0 and ((x*i)%10) !=y){
        i+=1;
    }
    cout<<i;
 
    return 0;
}