#include <iostream>
using namespace std;

int main()
{
    int n,t=0;
    string children;
   	cin >> n >> t;
   	cin >> children;

   
   	while(t!=0)
    {
  
	    	for(int i = 0; i<children.length(); i++) {
	
		      if(children[i] == 'B' && children[i+1] == 'G')
		      {
	
		      	children[i+1] = 'B';
		      	children[i] = 'G';
		    	i++;
			  } 
			    
		   }
		   
	   t--;
	}
    
    for(int x = 0; x<children.length(); x++) {
      cout << children[x];
   }
    
    
    
	return 0;
}


