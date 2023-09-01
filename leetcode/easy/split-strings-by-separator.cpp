#include <iostream>
#include <vector>

using namespace std;

vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
    string cur = "";
    vector<string> result;

    for (auto word : words) {
        for (auto c : word) {
            if (c == separator) {
                if (cur != "") {
                    result.push_back(cur);
                }
                cur = "";
            } else {
                cur += c;
            }
        }
        if (cur != "") {
            result.push_back(cur);
        }
        cur = "";
    }

    return result;
}

int main() {
    vector<string> words = {"one.two.three", "four.five", ".six."};
    vector<string> result = splitWordsBySeparator(words, '.');
    for (auto word : result) {
        cout << word << endl;
    }
}