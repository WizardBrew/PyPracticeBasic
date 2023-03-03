#include <iostream>

using namespace std;
                                                // Selection  control struct    ----- Switch case
int main()
{
    int age;
    cout << "Enter your Age " << endl;
    cin >> age;

    switch (age)
    {
    case 18:
        cout << "you are 18" << endl;
        break; // If Break is not used then rest of all case print below the executed op
    case 20:
        cout << "Your are 20" << endl;
        break;
    case 25:
        cout << "Your are 25" << endl;
        break;

    default:
        cout << "YOu Chose something out of Context" << endl;
        break;
    }
    cout<<"--- Successfully Executed Switch Case -- "<<endl;    // Once exec loop it will display outer msg
    return 0;
}