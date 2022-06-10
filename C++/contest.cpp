#include <bits/stdc++.h>
using namespace std;

int main()
{

  	
    ios_base::sync_with_stdio(false);
    int n,count=0;
    cin>>n;
    while(n!=0)
    {
	    int a,b,c;
	    cin>>a>>b>>c;
	    if(a==1 && b == 1 && c == 1)
	    {
	    	count++;
		}else if (a==1 &&  b == 1 && c== 0){
			count++;
		}
		else if(a==1 && b==0 && c==1)
		{
			count++;
		}else if(a==0 && b==1 && c ==1)
		{
			count++;
		}
		n--;
	}
	cout<<count;
	
	
	return 0;
}


