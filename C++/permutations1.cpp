#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int i,t,n;
    vector<int> fex = {};
    cin>>n;
    // for(i=0;i<t;i++)
    // {
    //     cin>>n;
    //     if(n%2 == 0)
    //     {
    //         for(int j=n;j>=1;j--)
    //         {
    //             cout<<j<<" ";
    //         }
    //     }
    //     else{
            for(int x=5;x > 1;x--)
            {
               
                fex.push_back(x); 
                swap(fex[n/2],fex[(n/2)+1]);
            }
            for(int fk=0;fk=n;fk++)
            {
                cout<<fex[fk]<<" ";
            }
//         }
//     }
 }