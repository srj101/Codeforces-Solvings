#include<bits/stdc++.h>

using namespace std;
int main(){
    int t;
    cin>> t;
    while (t--)
    {
        int n;
        cin>>n;
        if(n%2==0){
            for (int i=n;i>=1;i--)
            {
                /* code */
                cout << i << " ";
            }
        }
        else{
            for (int i = n, j=2; i>=1 && j<=n ; i-=2, j+=2)
            {
                /* code */
                cout<< j << " " << i << " ";
            } 
            cout<<1;
        }
        cout<< endl;
    }
      return 0;
}
