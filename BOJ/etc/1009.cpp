#include <cmath>
#include <iostream>

using namespace std;

int main() {
    int tc, a, b;

    cin >> tc;

    for (int i = 0; i < tc; i++) {
        cin >> a >> b;

        if (b % 4 == 0) {
            b = 4;
        } else {
            b %= 4;
        }

        int temp = pow(a, b);
        if (temp % 10 == 0)
            cout << 10 << endl;
        else
            cout << int(temp) % 10 << endl;
    }
}

// 5
// 1 6 = 1
// 3 7 = 7
// 6 2 = 6
// 7 100 = 1
// 9 635 = 9