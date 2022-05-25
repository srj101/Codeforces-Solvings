#include<iostream>
using namespace std;

int main()
{
    int X,f;
    cin>>X;
    X++;
    while(X%3 != 0)
    {
        X++;
    }
    cout<<X;
}