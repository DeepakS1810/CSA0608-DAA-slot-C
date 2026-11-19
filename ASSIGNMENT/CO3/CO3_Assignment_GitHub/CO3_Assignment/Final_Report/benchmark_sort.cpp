
#include <bits/stdc++.h>
using namespace std;
volatile long long sinkv=0;
void mergeF(vector<int>&a,int l,int m,int r){vector<int>x(a.begin()+l,a.begin()+m+1),y(a.begin()+m+1,a.begin()+r+1);int i=0,j=0,k=l;while(i<x.size()&&j<y.size())a[k++]=(x[i]<=y[j]?x[i++]:y[j++]);while(i<x.size())a[k++]=x[i++];while(j<y.size())a[k++]=y[j++];}
void ms(vector<int>&a,int l,int r){if(l>=r)return;int m=(l+r)/2;ms(a,l,m);ms(a,m+1,r);mergeF(a,l,m,r);}
int part(vector<int>&a,int l,int r){int p=a[r],i=l-1;for(int j=l;j<r;j++)if(a[j]<=p)swap(a[++i],a[j]);swap(a[i+1],a[r]);return i+1;}
void qs(vector<int>&a,int l,int r){if(l<r){int p=part(a,l,r);qs(a,l,p-1);qs(a,p+1,r);}}
int main(){mt19937 g(17); for(int n:{1000,3000,6000,10000}){vector<int>x(n);for(auto&v:x)v=g(); vector<double> tm, tq;for(int k=0;k<5;k++){auto a=x;auto t=chrono::steady_clock::now();ms(a,0,n-1);tm.push_back(chrono::duration<double,micro>(chrono::steady_clock::now()-t).count());sinkv+=a[0];a=x;t=chrono::steady_clock::now();qs(a,0,n-1);tq.push_back(chrono::duration<double,micro>(chrono::steady_clock::now()-t).count());sinkv+=a[0];}sort(tm.begin(),tm.end());sort(tq.begin(),tq.end());cout<<n<<","<<tm[2]<<","<<tq[2]<<"\n";}}
