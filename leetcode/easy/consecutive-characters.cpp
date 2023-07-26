#include <algorithm>
#include <iostream>

using namespace std;

int maxPower(string s) {
    char prev = s[0];
    int cnt = 1;

    int result = 1;
    for (int i = 1; i < s.length(); i++) {
        if (s[i] == prev) {
            cnt++;
            result = max(result, cnt);
        } else {
            cnt = 1;
            prev = s[i];
        }
    }

    return result;
}

int main() {
    int result = maxPower("leetcode");
    cout << result << endl;
}