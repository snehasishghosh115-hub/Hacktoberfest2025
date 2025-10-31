#include<iostream>
using namespace std;

int NaturalNum(int n)
{ 
 if(n>10)
 {
    return 0;
 }
 else
 {
    cout<<n<<endl;
    NaturalNum(n+1);
 }
}

int main()
{
    int n=1;
    NaturalNum(n);
    return 0;
    
}
