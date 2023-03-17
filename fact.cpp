#include<iostream>

using namespace std;

int main(){
        cout<<" Factorials "<< endl;
        int i =5, fact=1, sum=5;
        while(i>=1){
                fact = fact*i;
                i--;
                cout<<"fact => "<<fact<<endl;
        }
        return 0;
}