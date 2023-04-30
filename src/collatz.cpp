#include <iostream>

int main(void) {
    long int n {};
    std::cout << "Enter N: ";
    std::cin >> n;
    std::cout << n;
    while ( n != 1 ) {
        if ( n % 2 == 0 ) {
            n = n/2;

        } else {
            n = 3*n + 1;
        }
        std::cout << " " << n;
    }
    std::cout << std::endl;
    return 0;
}

