#include<iostream>

using namespace std;

int main(){
        cout<<"Factorial " << endl;
        int num =5, Fact=1;
        while(num>=2){
                Fact = num*Fact;
                num= num - 1;
                cout<<"Num => "<<num<<endl;
                cout<<"Fact => "<<Fact<<endl;
        }
        return 0;
}