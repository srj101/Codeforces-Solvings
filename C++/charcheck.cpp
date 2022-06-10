#include <bits/stdc++.h>
using namespace std;

int main()
{

  	
    ios_base::sync_with_stdio(false);
    int n;
    cin>>n;
    while(n!=0)
    {
	    string word;
		cin>>word;
		if(word.length() <= 10)
		{
			cout<<word<<endl;
		}else {
			cout<<word[0]<<word.length() - 2<<word[word.length() - 1]<<endl;
		}
		n--;
	}
	
	
	
	return 0;
}


