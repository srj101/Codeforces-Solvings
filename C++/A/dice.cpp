#include<iostream>
using namespace std;

int main()
{
    int H=0,D=0,n=1,nn=1,point;
    
    while(H!=6){
        cin>>H;
        if(H==6)
        {
            n++;
            cin>>H;
            H = H+(n*6);
            if(n == 3){
                if(H==6)
                {
                    H=0;
                }
            }
            else{
                H=H+((n%3)*6);
            }
        }else{
            cin>>H;
            break;
        }
    }
    // cin>>D;
    // if(D==6){
    //     while(D==6)
    //     {
    //         nn++;
    //         cin>>D;
    //         if(D!=6){
    //             break;
    //         }
    //         if(nn==12){
    //             if(D==6)
    //             {
    //                 D=0;
    //                 break; 
    //             }
    //         }  
    //     }
    // }
    // if(H>D){
    //     cout<<"Hablu Is Winner";
    // }
    // else if(H==D)
    // {
    //     cout<<"The Round Is Draw";
    // }
    // else{
    //     cout<<"Dablu Is Winner";
    // }
}