#include<iostream>

using namespace std;

int main(){
        cout<<"Prod of 3"<< endl;
        int i = 248, pro=1;
        while(i>1){
                pro= pro*(i%10);
                i=i/10;
                cout<<"Pro => "<<pro<<endl;
        }
        return 0;
}