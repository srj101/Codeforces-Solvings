#include <iostream>
#include <cmath>
#include<iomanip>
using namespace std;
 
int main()
{
    unsigned long long int t;
    cin>>t;
    while(t>0) {
        unsigned long long int a;
        cin>>a;
        cout<<fixed<<setprecision(0)<<floor((a-1)/2)<<endl;
        t--;
    }
    return 0;
}