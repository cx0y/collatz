#include <iostream>
using namespace std;

int main(void) {
    long int n {};
    cout << "Enter N: ";
    cin >> n;
    cout << n;
    while ( n != 1 ) {
        if ( n % 2 == 0 ) {
            n = n/2;

        } else {
            n = 3*n + 1;
        }
        cout << " " << n;
    }
    cout << endl;
    return 0;
}

