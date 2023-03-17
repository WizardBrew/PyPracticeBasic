#include<iostream>

using namespace std;

int main(){
        cout<<"Prime"<< endl;
        int i= 5, j=1, c=0;
        while(i>=j){
                if(i%j==0){
                        c++;
                } 
                j++;
        }
        cout<<c;

        return 0;
}