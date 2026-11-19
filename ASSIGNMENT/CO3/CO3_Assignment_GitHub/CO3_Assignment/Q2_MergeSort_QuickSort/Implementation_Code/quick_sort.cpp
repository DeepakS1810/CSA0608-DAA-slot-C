#include <iostream>
#include <vector>
using namespace std;
long long comparisons=0; int maxDepth=0;
int partitionLast(vector<int>& a,int low,int high) {
    int pivot=a[high], i=low-1;
    for(int j=low;j<high;j++) {
        ++comparisons;
        if(a[j]<=pivot) { ++i; swap(a[i],a[j]); }
    }
    swap(a[i+1],a[high]); return i+1;
}
void quickSort(vector<int>& a,int low,int high,int depth=1) {
    if(low<high) {
        if(depth>maxDepth) maxDepth=depth;
        int p=partitionLast(a,low,high);
        quickSort(a,low,p-1,depth+1);
        quickSort(a,p+1,high,depth+1);
    }
}
int main() {
    vector<int> a={9,4,7,3,10,5,1,8,2,6};
    quickSort(a,0,(int)a.size()-1);
    cout<<"Sorted: "; for(int x:a) cout<<x<<" ";
    cout<<"\nComparisons="<<comparisons<<"\nMaximum recursion depth="<<maxDepth<<"\n";
}
