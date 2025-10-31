#include<iostream>
using namespace std;

int fibonacci(int num)
{
    int num_a, num_b,num_c;
    num_a=0;
    num_b=1;
    cout<<num_a<<" , ";
    cout<<num_b<<" , ";
    int i=1;
    while (i<=num)
    {
        num_c=num_a+num_b;
        num_a=num_b;
        num_b=num_c;
        cout<<num_c<<" , ";
        i++;
    }
    return 0;
    

}

int recuersive_fibonacci( int num , int num_a,int num_b , int num_c )
{
   
    if(num<=0)
    {
        return 0;
    }
    num_c=num_a+num_b;
    num_a=num_b;
    num_b=num_c;
    cout<<num_c<<" , ";
    recuersive_fibonacci(num-1,num_a, num_b, num_c);
    

}
int main()
{
 int num;
 cout<<"Enter the number of sequences you want : ";
 cin>>num;
//  fibonacci(num);
 int num_a,num_b,num_c;
 num_a=0;
 num_b=1;
 cout<<num_a<<" , ";
 cout<<num_b<<" , ";
recuersive_fibonacci(num-2, num_a,num_b,num_c);
 

}
