#include <iostream>
using namespace std;
int main()
{
    int testCase;
    cin>>testCase;
    
    while(testCase > 0){
        int boxSize;
        cin>>boxSize;
        int candies[boxSize];
        for(int i=0;i<boxSize;i++){
            cin>>candies[i];
        }
        int min = candies[0];
        for(int i = 1; i < boxSize; i++)
    	{
    		if(min > candies[i])
    			min = candies[i];
    	}
    	
    	int k = 0;
        while (k < boxSize)
        {
            if (candies[k] == min) {
                break;
            }
            k++;
        }
        int ans=0;
        for(int i=0;i<boxSize;i++) {
            if(i==k) {
                continue;
            }else {
                ans += candies[i];
            }
        }
        cout<<ans-min*(boxSize-1)<<endl;
        testCase--;
    }
 
    return 0;
}