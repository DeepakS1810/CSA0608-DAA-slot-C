#include <iostream>
#include <vector>
using namespace std;
int binarySearch(const vector<int>& a, int target, long long& cmp) {
    int low=0, high=(int)a.size()-1;
    while(low<=high) {
        int mid=low+(high-low)/2;
        ++cmp;
        if(a[mid]==target) return mid;
        ++cmp;
        if(a[mid]<target) low=mid+1;
        else high=mid-1;
    }
    return -1;
}
int main() {
    vector<int> a={2,5,8,12,16,23,38,56,72,91};
    for(int target : {23,24}) {
        long long c=0; int index=binarySearch(a,target,c);
        cout<<"Target "<<target<<": ";
        if(index>=0) cout<<"found at index "<<index;
        else cout<<"not found";
        cout<<", comparisons="<<c<<"\n";
    }
}
