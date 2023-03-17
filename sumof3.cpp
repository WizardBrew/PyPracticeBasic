#include<iostream>

using namespace std;

int main(){
        cout<<"Sum of 3"<< endl;
        int i =248, sum = 0;
        while(i>0){
                sum = sum+(i%10);
                i= i/10;
                cout<<"Sum => "<<sum<<endl;
        }
        return 0;
}