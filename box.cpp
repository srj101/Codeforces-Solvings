#include <bits/stdc++.h>
 
#define     int            long long


using namespace std;


signed main()
{

    int F;
	cin>>F;
	int x=1;
	int jahobe=(F-2*x) *(F-2*x) *x;

	for(int i=1; i<=F; i++)
	{   
		x++;
		if((F-2*x)<=0)
		{
			x--;
			break;
		}
		int myguess= (F-2*x) *(F-2*x) *x;
		
		
		
	
		if(myguess<jahobe)
		{ 
			x--;
			break;
		}
		else
		{
			jahobe=myguess;
		}
	

		
	}
	cout << jahobe << " " << x << endl;



}