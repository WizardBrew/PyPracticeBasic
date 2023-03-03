#include<iostream>

using namespace std;
void brk(){
 for (int  i = 0; i < 10; i++)
    {
        // cout<<i<<endl;      //if defined first it will print and exit
        if(i ==5){      
            break;           // once you get at point it will exit immediate
        }
        cout<<i<<endl; // if defined after it will not print exits before
        }
}   

void cntnu(){
   for (int i = 0; i < 10; i++)  {
    // cout<<i<<endl;                   // Never Mention Before Wrong Logic
    if(i == 5){
        continue;
    }
    cout<<i<<endl;              // Skips and continue once its reached to condition
   }
    
}

int main(){
    cout<<"tut 11"<<endl;

    // brk();
    cntnu();
    return 0;
}