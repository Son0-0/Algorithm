#include <iostream>
#include <string>

using namespace std;

string toLowerCase(string s) {
    for (int i = 0; i < s.size(); i++) {
        s[i] = tolower(s[i]);
    }

    return s;
}

int main() { cout << toLowerCase("Hello") << endl; }