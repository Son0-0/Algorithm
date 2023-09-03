#include <iostream>
#include <vector>

using namespace std;

bool canConstruct(string ransomNote, string magazine) {
    vector<int> alpha(26, 0);

    for (auto c : magazine) {
        alpha[c - 'a']++;
    }

    for (auto c : ransomNote) {
        if (alpha[c - 'a'] < 0) {
            return false;
        } else {
            alpha[c - 'a']--;
        }
    }

    return true;
}

int main() { cout << canConstruct("aa", "aab") << endl; }