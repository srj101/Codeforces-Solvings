#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
   int findLengthOfLCIS(vector<long long>& nums) {
      if (nums.size() <= 1)
         return nums.size();
      int answer = 1, count = 1;
      for (int i = 0; i < nums.size() - 1; i++) {
         if (nums[i] <= nums[i + 1]) {
            count++;
            answer = max(answer, count);
         }
         else {
            count = 1;
         }
      }
      return answer;
   }
};
main(){
   Solution ob;
   vector<long long> v;
   long long n,a;
   cin>>n;
   for(int i=0;i<n;i++)
    {
      cin>>a;
      v.push_back(a);
    }
   cout << (ob.findLengthOfLCIS(v));
}