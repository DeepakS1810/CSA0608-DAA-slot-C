#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
long long standardCount=0, karatsubaCount=0;
string addStr(string a,string b) {
    string r; int i=(int)a.size()-1,j=(int)b.size()-1,carry=0;
    while(i>=0||j>=0||carry) {
        int s=carry+(i>=0?a[i--]-'0':0)+(j>=0?b[j--]-'0':0);
        r.push_back(char('0'+s%10)); carry=s/10;
    }
    reverse(r.begin(),r.end()); return r;
}
string subStr(string a,string b) { // assumes a >= b
    int i=(int)a.size()-1,j=(int)b.size()-1,borrow=0;
    string r;
    while(i>=0) {
        int d=(a[i--]-'0')-borrow-(j>=0?b[j--]-'0':0);
        if(d<0) d+=10,borrow=1; else borrow=0;
        r.push_back(char('0'+d));
    }
    while(r.size()>1 && r.back()=='0') r.pop_back();
    reverse(r.begin(),r.end()); return r;
}
string shift10(string a,int n) { if(a=="0") return a; return a+string(n,'0'); }
string norm(string a) { size_t p=a.find_first_not_of('0'); return p==string::npos?"0":a.substr(p); }
string standardMul(string a,string b) {
    a=norm(a); b=norm(b); string r(a.size()+b.size(),'0');
    for(int i=(int)a.size()-1;i>=0;i--) for(int j=(int)b.size()-1;j>=0;j--) {
        ++standardCount; int v=(r[i+j+1]-'0')+(a[i]-'0')*(b[j]-'0');
        r[i+j+1]=char('0'+v%10); r[i+j]+=v/10;
    }
    return norm(r);
}
string karatsuba(string x,string y) {
    x=norm(x); y=norm(y);
    if(x.size()<=2 || y.size()<=2) {
        // Count one small base multiplication for each digit pair.
        string z="0";
        for(char a:x) for(char b:y) ++karatsubaCount;
        return standardMulNoCount(x,y);
    }
    int n=max(x.size(),y.size()); if(n%2) ++n;
    x=string(n-x.size(),'0')+x; y=string(n-y.size(),'0')+y;
    int m=n/2;
    string a=x.substr(0,m), b=x.substr(m), c=y.substr(0,m), d=y.substr(m);
    string ac=karatsuba(a,c), bd=karatsuba(b,d);
    string abcd=karatsuba(addStr(a,b),addStr(c,d));
    string mid=subStr(subStr(abcd,ac),bd);
    return norm(addStr(addStr(shift10(ac,2*m),shift10(mid,m)),bd));
}
string standardMulNoCount(string a,string b) {
    string r(a.size()+b.size(),'0');
    for(int i=(int)a.size()-1;i>=0;i--) for(int j=(int)b.size()-1;j>=0;j--) {
        int v=(r[i+j+1]-'0')+(a[i]-'0')*(b[j]-'0');
        r[i+j+1]=char('0'+v%10); r[i+j]+=v/10;
    }
    return norm(r);
}
int main() {
    string a="12345678901234567890", b="98765432109876543210";
    string x=standardMul(a,b), y=karatsuba(a,b);
    cout<<"Standard product: "<<x<<"\nKaratsuba product: "<<y
        <<"\nEqual results: "<<(x==y?"yes":"no")
        <<"\nStandard digit multiplications: "<<standardCount
        <<"\nKaratsuba base digit multiplications: "<<karatsubaCount<<"\n";
}
