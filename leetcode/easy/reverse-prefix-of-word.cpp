#include <iostream>

using namespace std;

string reversePrefix(string word, char ch) {
    int target = -1;

    for (int i = 0; i < word.size(); i++) {
        if (word[i] == ch) {
            target = i;
            break;
        }
    }

    if (target == -1) {
        return word;
    } else {
        string result = "";

        for (int i = target; i >= 0; i--) {
            result += word[i];
        }

        for (int i = target + 1; i < word.size(); i++) {
            result += word[i];
        }

        return result;
    }
}

int main() {
    string result = reversePrefix("abcdefd", 'd');
    cout << result << endl;
}