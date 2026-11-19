#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
using namespace std;
struct Point{double x,y;};
struct Answer{double d; Point a,b; long long checks;};
double dist2(const Point&a,const Point&b){double x=a.x-b.x,y=a.y-b.y;return x*x+y*y;}
Answer brute(const vector<Point>&p) {
    Answer z{numeric_limits<double>::infinity(),{}, {},0};
    for(int i=0;i<(int)p.size();i++) for(int j=i+1;j<(int)p.size();j++) {
        ++z.checks; double d=dist2(p[i],p[j]); if(d<z.d)z={d,p[i],p[j],z.checks};
    } return z;
}
Answer solve(vector<Point> px, vector<Point> py) {
    int n=px.size(); if(n<=3)return brute(px);
    int mid=n/2; double midx=px[mid].x;
    vector<Point> lx(px.begin(),px.begin()+mid), rx(px.begin()+mid,px.end());
    vector<Point> ly,ry;
    for(auto p:py) (p.x<midx || (p.x==midx && ly.size()<lx.size())?ly:ry).push_back(p);
    Answer L=solve(lx,ly), R=solve(rx,ry);
    Answer best=L.d<R.d?L:R; best.checks=L.checks+R.checks;
    vector<Point> strip; for(auto p:py) if((p.x-midx)*(p.x-midx)<best.d)strip.push_back(p);
    for(int i=0;i<(int)strip.size();i++) for(int j=i+1;j<(int)strip.size() && (strip[j].y-strip[i].y)*(strip[j].y-strip[i].y)<best.d;j++) {
        ++best.checks; double d=dist2(strip[i],strip[j]); if(d<best.d){best.d=d;best.a=strip[i];best.b=strip[j];}
    }
    return best;
}
int main() {
    vector<Point> p={{2,3},{12,30},{40,50},{5,1},{12,10},{3,4},{8,9}};
    Answer b=brute(p);
    vector<Point> px=p,py=p;
    sort(px.begin(),px.end(),[](Point a,Point b){return a.x<b.x;});
    sort(py.begin(),py.end(),[](Point a,Point b){return a.y<b.y;});
    Answer d=solve(px,py);
    cout<<"Brute closest distance="<<sqrt(b.d)<<" distance checks="<<b.checks<<"\n";
    cout<<"D&C closest distance="<<sqrt(d.d)<<" distance checks="<<d.checks<<"\n";
}
