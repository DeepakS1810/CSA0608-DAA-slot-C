#include <iostream>
#include <vector>
#include <utility>
using namespace std;
struct Result { int mn, mx; long long comparisons; };
Result maxMin(const vector<int>& a, int l, int r) {
    if (l == r) return {a[l], a[l], 0};
    if (r == l + 1) {
        if (a[l] < a[r]) return {a[l], a[r], 1};
        return {a[r], a[l], 1};
    }
    int m = l + (r-l)/2;
    Result x=maxMin(a,l,m), y=maxMin(a,m+1,r);
    return {min(x.mn,y.mn), max(x.mx,y.mx),
            x.comparisons+y.comparisons+2};
}
int main() {
    vector<int> a={8,3,12,5,1,9,14,6};
    Result r=maxMin(a,0,(int)a.size()-1);
    cout<<"Minimum = "<<r.mn<<"\nMaximum = "<<r.mx
        <<"\nComparisons = "<<r.comparisons<<"\n";
}
