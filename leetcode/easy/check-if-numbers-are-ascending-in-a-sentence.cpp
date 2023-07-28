#include <iostream>
#include <vector>

using namespace std;

vector<string> split(string str, char delimeter) {
    vector<string> result;
    string temp;

    for (int i = 0; i < str.length(); i++) {
        if (str[i] == delimeter) {
            result.push_back(temp);
            temp.clear();
        } else {
            temp.push_back(str[i]);
            if (i == str.length() - 1) {
                result.push_back(temp);
            }
        }
    }

    return result;
}

bool areNumbersAscending(string s) {
    vector<string> target = split(s, ' ');

    int num = 0;
    for (auto token : target) {
        if (isdigit(token[0])) {
            int temp = stoi(token);
            if (num < temp) {
                num = temp;
            } else {
                return false;
            }
        }
    }

    return true;
}

int main() {
    bool result = areNumbersAscending("5 x 5");

    cout << result << endl;
}