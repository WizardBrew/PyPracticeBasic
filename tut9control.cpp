#include<iostream>

using namespace std;
int main(){
                                // 1)Sequence Structrue       2) Selection Struct     3) Loop Struct (Tut10 = ref)
    int age;
    cout<<"Enter your age "<<endl;
    cin>>age;
    if(age<18){
        cout<<"You cannot Vote"<<endl;
    }
    else if (age==18){
        cout<<"You are reached to age of Vote get Pass"<<endl;
    }
    else{
        cout<<"YOu can Vote"<<endl;
    }

    return 0;
}