#include <iostream>
#include <string>

using namespace std;

string intToBin(int n) {
    if (n == 0) {
        return "0";
    }

    string result = "";

    while (n > 0) {
        result = to_string(n % 2) + result;
        n /= 2;
    }

    return result;
}

int bitwiseComplement(int n) {
    string target = intToBin(n);
    int mul = 1;

    int result = 0;
    for (int i = target.size() - 1; i >= 0; i--) {
        if (target[i] == '0') {
            result += mul;
        }
        mul *= 2;
    }

    return result;
}

int main() { cout << bitwiseComplement(10) << endl; }