#include <iostream>
#include <unordered_map>

using namespace std;

bool isThree(int n) {
    unordered_map<int, bool> um;

    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            um[i] = true;
        }
    }

    return um.size() == 3;
}

int main() {
    bool result = isThree(4);
    cout << result << endl;
}