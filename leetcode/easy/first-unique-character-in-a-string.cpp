#include <iostream>
#include <unordered_map>

using namespace std;

int firstUniqChar(string s) {
    unordered_map<char, int> um;

    for (auto c : s) {
        um[c]++;
    }

    for (int i = 0; i < s.size(); i++) {
        auto temp = um.find(s[i]);
        if (temp->second == 1) {
            return i;
        }
    }

    return -1;
}

int main() {
    int result = firstUniqChar("leetcode");
    cout << result << endl;
}