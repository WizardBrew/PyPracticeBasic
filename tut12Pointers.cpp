#include<iostream>

using namespace std;
                                // & - is Address of 
                                // * - Pointer
int main(){
    int Num = 40;
    int* NumAddr = &Num;
    int** c =  &NumAddr;

    // cout<<"The Num is - "<<Num<<endl;           // Saved Variable in Num
    // cout<<"The Num is - "<<&Num<<endl;           // Saved Variable in Num Address same Below
    // cout<<"The NumAddr is - "<<NumAddr<<endl;   // Created Pointer with * and &Pointing.
    // cout<<"The Derefereance of NumAddr - "<<*NumAddr<<endl;     // if used *Pointer shows what it holds
    // cout<<"----------------==========-----------------"<<endl;

    // cout<<"The RnD - "<<&Num<<endl;     // - Shows Address of
    // cout<<"The RnD - "<<NumAddr<<endl;  // Pointer created as variable pointing &Num 

    cout<<"The Pointer "<<&Num<<endl;
    cout<<"Pointer Add "<<*NumAddr<<endl;



    return 0;
}