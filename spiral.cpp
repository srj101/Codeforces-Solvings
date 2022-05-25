 

 #include<iostream>
 using namespace std;
 #define ll long long
 
 void solve(){
 ll row, col;
 cin>> row>> col;
 ll ans=0;
 
 if (row < col)
 {
     if (col%2!=0)
     {
         ans = (col*col) - row +1;
     }
     else
     {
         ans = (col-1) * (col-1) + row;
     }
 }
 else
 {
     if (row % 2!=0)
     {
 
         ans = (row-1) * (row-1) + col;
 
     }
     else
     {
          ans = (row * row) -  col + 1;
 
     }
 }
 cout << ans << endl;
 
 
 
 
}

int main()
{
    solve();
}