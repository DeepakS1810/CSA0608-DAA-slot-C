#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<long long> sums(const vector<int>& a,int l,int r) {
    vector<long long> s={0};
    for(int i=l;i<r;i++) {
        int old=s.size(); for(int j=0;j<old;j++)s.push_back(s[j]+a[i]);
    } return s;
}
bool subsetSumMITM(const vector<int>& a,long long target) {
    int mid=a.size()/2;
    vector<long long> L=sums(a,0,mid), R=sums(a,mid,a.size());
    sort(R.begin(),R.end());
    for(long long x:L) if(binary_search(R.begin(),R.end(),target-x))return true;
    return false;
}
int main() {
    vector<int> a={3,34,4,12,5,2}; long long target=9;
    cout<<"Target "<<target<<(subsetSumMITM(a,target)?" can":" cannot")<<" be formed\n";
    cout<<"Half subset counts: "<<(1u<<(a.size()/2))<<" and "<<(1u<<(a.size()-a.size()/2))<<"\n";
}
