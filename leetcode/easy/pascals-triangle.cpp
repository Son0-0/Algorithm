#include <iostream>
#include <vector>

using namespace std;

vector<int> generateRow(int row) {
    int cur = 1;
    vector<int> result;

    result.push_back(cur);

    for (int col = 1; col < row; col++) {
        cur = cur * (row - col);
        cur = cur / col;
        result.push_back(cur);
    }

    return result;
}

vector<vector<int>> generate(int numRows) {
    vector<vector<int>> result;

    for (int i = 1; i <= numRows; i++) {
        result.push_back(generateRow(i));
    }

    return result;
}

int main() {
    vector<vector<int>> result = generate(5);

    for (auto arr : result) {
        for (auto num : arr) {
            cout << num << endl;
        }
    }
}