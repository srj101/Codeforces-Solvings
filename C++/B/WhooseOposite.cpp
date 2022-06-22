#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
 
void solve(){
	int a,b,c,peoples;
    vector<int> numbers;
    int size;
    size = numbers.size();
    
    
    cin>>a>>b>>c;
    int diff;
    diff = abs(a-b);
    peoples = diff*2;
    
    if(c>peoples || a > peoples || b > peoples){
    	cout << -1<<endl;
	}
	else{
	    if(c<diff){
	    	if(a<=diff){
		    	cout <<  c + diff<< endl;
			}
			else if(a>=diff)
			{
				if(c-diff<0){
					cout <<  c + diff<< endl;
				}
				else {
					cout << c - diff<< endl;
				}
			}
		}
		else if (c == diff){
			cout <<  c + diff<< endl;
		}
		else {
			cout << c - diff<< endl;
		}
	}
}
 
 
int main()
{
	
	int t=1;
	   cin>>t;
	   while(t--)
	   solve();
	   
    
 
}