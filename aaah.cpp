#include <iostream>
#include <string>
using namespace std;

int main(){
    string n;
    string m;
    cin >> n >> m;

    if(n.size() >= m.size()){
        cout << "goo";
    } else{
        cout << "no";
    }

    return 0;
}