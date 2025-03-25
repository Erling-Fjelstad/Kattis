#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main(){

    int n; 
    cin >> n;
    cin.ignore();  

    string line;
    getline(cin, line);  

    vector<string> friends; 
    stringstream ss(line);  
    string name;
    
    while (ss >> name) {
        friends.push_back(name);
    }

    int N = 13;

    int rest = (N - 1) % n;  

    cout << friends.at(rest) << endl;

    return 0;
}