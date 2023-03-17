#include<iostream>

using namespace std;

int main(){
        cout<<"Natural Sum"<< endl;
        int i=1, sum=0;
        while (i<=10){
                sum = sum+i;
               i =  i+1;
                cout<< "Sum =>  "<<sum<<endl;
        }
        return 0;
}