#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
using namespace std;


void reversestring(string& str)
{
    int n = str.length();
    for(int i=0;i<n/2;i++)
    {
        swap(str[i],str[n-i-1]);
    }
}

int main() {
    string A,ADDED,F;
    char C;
    char BC;
    int N,L,count=0;

    cin>>N;

    for(int i=0;i<N;i++)
    {
       
       count = count +1;
       if(count>3)
       {
           continue;
       }
     }
    string B = "";

    switch (count)
    {
    case 1:
        cin>>L;
        cin >> BC;                                                  // input B
        for (int i = 0; i < L; i++){
            B = B + C;
        }
        cin>>C;
        ADDED = A+B;
        reversestring(ADDED);
        
        F = ADDED;

        break;
    case 2:
        if(C == 'E'){
            ADDED = ADDED + B; 
        }
        break;
    case 3:
        if ( C == 'B'){
            ADDED = B + ADDED;
        }
        break;
    default:
        break;
    }


    cout<<ADDED;
    return 0;
}

