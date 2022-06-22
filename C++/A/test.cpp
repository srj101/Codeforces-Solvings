#include <iostream>
using namespace std;

int main()
{
    int n, a ,b,c,sumX=0,sumY=0,sumZ=0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        
        	cin>>a>>b>>c;
        	sumX += a;
        	sumY += b;
        	sumZ += c;
		
		
    }
    
    if (sumX ==0 && sumY == 0 && sumZ == 0){
    	cout<<"YES"<<endl;
	}else {
		cout <<"NO"<<endl;
	}
	
	return 0;
}
