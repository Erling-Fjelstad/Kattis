#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
    int n;
    cin >> n;

    long double eulersNumber = 1.0;  
    long double factorial = 1.0;     

    for (int i = 1; i <= n; i++) {
        factorial *= i;  
        eulersNumber += 1.0 / factorial;
    }

    cout << fixed << setprecision(13) << eulersNumber << endl;
    return 0;
}