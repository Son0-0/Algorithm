#include <algorithm>
#include <cctype>
#include <iostream>

using namespace std;

string licenseKeyFormatting(string s, int k) {
    string parsedS = "";

    for (auto c : s) {
        if (isalpha(c)) {
            parsedS += toupper(c);
        } else if (isdigit(c)) {
            parsedS += c;
        }
    }

    string result = "";
    int temp = 0;

    for (int i = parsedS.size() - 1; i >= 0; i--) {
        if (temp == k) {
            temp = 0;
            result += "-";
        }
        result += parsedS[i];
        temp++;
    }

    reverse(result.begin(), result.end());

    return result;
}

int main() {
    string result = licenseKeyFormatting("5F3Z-2e-9-w", 4);
    cout << result << endl;
}