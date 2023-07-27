#include <iostream>

using namespace std;

int percentageLetter(string s, char letter) {
    float length = s.length();
    float cnt = 0;
    for (float i = 0; i < length; i++) {
        if (s[i] == letter) {
            cnt++;
        }
    }

    return (100 * cnt) / length;
}

int main() {
    int result = percentageLetter("leetcode", 'o');
    cout << result << endl;
}