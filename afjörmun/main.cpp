#include <iostream>
#include <string>

using namespace std;

int main() {
    int n; 
    cin >> n;
    cin.ignore(); 

    for (int i = 0; i < n; i++) {
        string sentence;
        getline(cin, sentence); 

        for (char &c : sentence) {
            c = tolower(c);
        }

        if (!sentence.empty()) {
            sentence[0] = toupper(sentence[0]);
        }

        cout << sentence << endl;
    }

    return 0;
}