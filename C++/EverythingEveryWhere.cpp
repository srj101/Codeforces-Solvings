#include <iostream>
#include <cmath>
using namespace std;
 
double arrayAvrg(double arr[],int Size) {
    double sum = 0;
    double avg = 0;
    for (int i = 0; i < Size; i++)
	{
		sum = sum + arr[i];
	}
	avg = (double)sum / Size;
	return avg;
}
 
bool search(double arr[], int n, double x)
{
    int i;
    for (i = 0; i < n; i++)
        if (arr[i] == x)
            return true;
    return false;
}
 
int main()
{
    int t;
    cin>>t;
    
    while(t>0) {
        int n;
        cin>>n;
        double arr[n];
        for(int i=0;i<n;i++) {
            cin>>arr[i];
        }
        
        if(search(arr,n,arrayAvrg(arr,n))){
            cout<<"YES"<<endl;
        }else {
            cout<<"NO"<<endl;
        }
        t--;
    }
 
    return 0;
}