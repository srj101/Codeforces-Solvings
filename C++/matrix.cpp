#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n[6][6],move=0;
    for (int i=1;i<=5;i++){
    	for(int j=1;j<=5;j++){
    		cin>>n[i][j];
		}
	}
	for (int x=1;x<=5;x++){
    	for(int y=1;y<=5;y++){
    		
    		
    		if(n[x][y] == 1){
    			
    			int u = x;
    			int q = y;
    			while (q!=3){
    				move++;
    				if(q>3){
    					q--;
					}else {
						q++;
					}
				}
    			while(u !=3){
    				move++;
    				if(u>3){
    					u--;
					}else {
						u++;
					}
				}
				
				
				
			}
		}
		
		
	}
	
	cout<<move;
	return 0;
}
