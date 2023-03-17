#include<iostream>

using namespace std;

int main(){
        cout<<"Palindrome"<< endl;
        int i=242, orig=i, rev=0;
        while(i>0){
                rev = (rev*10)+(i%10);
                i= i/10;
                cout<<"rev Check = > "<<rev<<endl;
        }
        if(rev == orig){
                cout<<"palind "<<endl;
        }
        else{
                cout<<"Not A Palind"<<endl;
        }
        return 0;
}