#include<iostream>

using namespace std;

int main(){
    int i=0;
            // While Loop
    //  While(Condition) { Statement}

    // while(true){             //initialize -----====-----  Never Do Crash Memory -- Always set exec or end point
// /*
    while(i <= 40){             //initialize
        cout<<i<<endl;      //condition 
        i++;                            //Update
    }
    cout<<"Done"<<endl;
    // */
    cout<<"===========================";

    // Also Checks if the condition has Already ran then it will not exec
    do{             // No matter what it while Run once loop    
        cout<<i<<endl;      //condition 
        i++;                            //Update
    }while (i<= 20);         //initialize
    
    
    cout<<"Done"<<endl;
    

    return 0;
}