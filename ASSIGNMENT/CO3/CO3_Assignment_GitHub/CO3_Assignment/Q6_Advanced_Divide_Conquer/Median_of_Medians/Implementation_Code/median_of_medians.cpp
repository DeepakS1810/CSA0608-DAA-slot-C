#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int selectK(vector<int>& a,int k) {
    if(a.size()<=5){sort(a.begin(),a.end());return a[k];}
    vector<int> med;
    for(size_t i=0;i<a.size();i+=5) {
        vector<int> g(a.begin()+i,a.begin()+min(a.size(),i+5));
        sort(g.begin(),g.end()); med.push_back(g[g.size()/2]);
    }
    int pivot=selectK(med,(int)med.size()/2);
    vector<int> low,eq,high;
    for(int x:a) {if(x<pivot)low.push_back(x);else if(x>pivot)high.push_back(x);else eq.push_back(x);}
    if(k<(int)low.size())return selectK(low,k);
    if(k<(int)(low.size()+eq.size()))return pivot;
    return selectK(high,k-(int)low.size()-(int)eq.size());
}
int main() {
    vector<int> a={12,3,5,7,4,19,26,1,9,15,2,8,11};
    int k=5; // zero-based: sixth smallest
    cout<<k+1<<"-th smallest = "<<selectK(a,k)<<"\n";
}
