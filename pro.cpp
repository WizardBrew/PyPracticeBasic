#include<iostream>

using namespace std;

int main(){
        cout<<"Prod"<< endl;
        int i= 1 , pro=1;
        while(i<=10){
                pro= pro*i;
                i= i+1;
                cout<<"Pro => "<<pro<<endl;
        }
        return 0;
}