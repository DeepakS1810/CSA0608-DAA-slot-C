#include <iostream>
#include <vector>
using namespace std;
using Matrix=vector<vector<long long>>;
Matrix addM(const Matrix&A,const Matrix&B,int sign=1) {
    int n=A.size(); Matrix C(n,vector<long long>(n));
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) C[i][j]=A[i][j]+sign*B[i][j];
    return C;
}
Matrix conventional(const Matrix&A,const Matrix&B) {
    int n=A.size(); Matrix C(n,vector<long long>(n));
    for(int i=0;i<n;i++) for(int k=0;k<n;k++) for(int j=0;j<n;j++) C[i][j]+=A[i][k]*B[k][j];
    return C;
}
Matrix quadrant(const Matrix&A,int r,int c,int h) {
    Matrix X(h,vector<long long>(h));
    for(int i=0;i<h;i++) for(int j=0;j<h;j++) X[i][j]=A[r+i][c+j];
    return X;
}
void place(Matrix&C,const Matrix&X,int r,int c) {
    int h=X.size(); for(int i=0;i<h;i++) for(int j=0;j<h;j++) C[r+i][c+j]=X[i][j];
}
Matrix strassen(const Matrix&A,const Matrix&B) {
    int n=A.size(); if(n<=2) return conventional(A,B);
    int h=n/2;
    Matrix a=quadrant(A,0,0,h), b=quadrant(A,0,h,h), c=quadrant(A,h,0,h), d=quadrant(A,h,h,h);
    Matrix e=quadrant(B,0,0,h), f=quadrant(B,0,h,h), g=quadrant(B,h,0,h), q=quadrant(B,h,h,h);
    Matrix m1=strassen(addM(a,d),addM(e,q));
    Matrix m2=strassen(addM(c,d),e);
    Matrix m3=strassen(a,addM(f,q,-1));
    Matrix m4=strassen(d,addM(g,e,-1));
    Matrix m5=strassen(addM(a,b),q);
    Matrix m6=strassen(addM(c,a,-1),addM(e,f));
    Matrix m7=strassen(addM(b,d,-1),addM(g,q));
    Matrix c11=addM(addM(addM(m1,m4),m5,-1),m7);
    Matrix c12=addM(m3,m5), c21=addM(m2,m4);
    Matrix c22=addM(addM(addM(m1,m2,-1),m3),m6);
    Matrix C(n,vector<long long>(n));
    place(C,c11,0,0); place(C,c12,0,h); place(C,c21,h,0); place(C,c22,h,h);
    return C;
}
int nextPow2(int n){int p=1;while(p<n)p*=2;return p;}
Matrix padded(const Matrix&A,int p) {
    Matrix P(p,vector<long long>(p));
    for(int i=0;i<(int)A.size();i++) for(int j=0;j<(int)A.size();j++) P[i][j]=A[i][j];
    return P;
}
int main() {
    Matrix A={{1,7,2},{3,5,4},{6,8,9}}, B={{1,3,2},{7,5,1},{4,2,6}};
    int n=A.size(), p=nextPow2(n);
    Matrix AP=padded(A,p), BP=padded(B,p), C=strassen(AP,BP), D=conventional(AP,BP);
    bool ok=true; cout<<"Product (top-left original dimension):\n";
    for(int i=0;i<n;i++){for(int j=0;j<n;j++){cout<<C[i][j]<<" "; if(C[i][j]!=D[i][j])ok=false;}cout<<"\n";}
    cout<<"Padded dimension="<<p<<"\nCorrectness check="<<(ok?"PASS":"FAIL")<<"\n";
}
