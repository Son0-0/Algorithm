#include <iostream>
#include <vector>

using namespace std;

void duplicateZeros(vector<int>& arr) {
    vector<int> copied(arr.begin(), arr.end());

    int cur = 0;
    for (int i = 0; i < copied.size(); i++) {
        if (copied[i] == 0) {
            arr[cur++] = copied[i];
        }

        if (cur == copied.size()) {
            return;
        }

        arr[cur++] = copied[i];

        if (cur == copied.size()) {
            return;
        }
    }
}

int main() { cout << "Hello Leetcode" << endl; }