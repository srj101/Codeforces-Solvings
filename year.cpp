#include <bits/stdc++.h>
using namespace std;

int main()
{

  
    ios_base::sync_with_stdio(false);
	int y;
    cin >> y;
	
	
	
	while(1)
	{
		y++;
		int a = y%10;
		int b = y / 10%10;
		int c = y / 100%10;
		int d = y / 1000%10;
		if(a!=b && a!=c && a !=d && b!=c && b!=d && c!=d)
		{
			cout <<y;
			break;
		}
	}
	
	return 0;
}


