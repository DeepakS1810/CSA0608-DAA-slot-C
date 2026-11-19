#include <iostream>
#include <vector>
using namespace std;
long long comparisons=0;
void mergeParts(vector<int>& a,int l,int m,int r) {
    vector<int> L(a.begin()+l,a.begin()+m+1), R(a.begin()+m+1,a.begin()+r+1);
    int i=0,j=0,k=l;
    while(i<(int)L.size() && j<(int)R.size()) {
        ++comparisons;
        if(L[i]<=R[j]) a[k++]=L[i++]; else a[k++]=R[j++];
    }
    while(i<(int)L.size()) a[k++]=L[i++];
    while(j<(int)R.size()) a[k++]=R[j++];
}
void mergeSort(vector<int>& a,int l,int r) {
    if(l>=r) return;
    int m=l+(r-l)/2;
    mergeSort(a,l,m); mergeSort(a,m+1,r); mergeParts(a,l,m,r);
}
int main() {
    vector<int> a={38,27,43,3,9,82,10};
    mergeSort(a,0,(int)a.size()-1);
    cout<<"Sorted: "; for(int x:a) cout<<x<<" ";
    cout<<"\nMerge comparisons="<<comparisons<<"\n";
}
