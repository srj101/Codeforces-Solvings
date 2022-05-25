#include<iostream>
using namespace std;

int main()
{
    int X,Total=0,R,RT=0;
    cin>>X;
    for(int i=1;i<=X;i++)
    {
        Total = Total + i;
    }
   for(int x=1;x<X;x++)
   {
       cin>>R;
       RT = RT+R;
   }

   cout<<(Total-RT);
}