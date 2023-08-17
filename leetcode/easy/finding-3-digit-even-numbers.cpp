#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

vector<int> findEvenNumbers(vector<int>& digits) {
    sort(digits.begin(), digits.end());

    int size = digits.size();
    set<int> s;

    for (int i = 0; i < size; i++) {
        if (digits[i] == 0) {
            continue;
        }
        for (int j = 0; j < size; j++) {
            if (i == j) {
                continue;
            }
            for (int k = 0; k < size; k++) {
                if (digits[k] % 2 == 1 || k == i || k == j) {
                    continue;
                }
                s.insert(100 * digits[i] + 10 * digits[j] + digits[k]);
            }
        }
    }

    vector<int> result(s.begin(), s.end());

    return result;
}

int main() {
    vector<int> digits = {2, 1, 3, 0};
    vector<int> result = findEvenNumbers(digits);

    for (auto item : result) {
        cout << item << endl;
    }
}