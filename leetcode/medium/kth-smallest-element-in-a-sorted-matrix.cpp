#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int kthSmallest(vector<vector<int>> &matrix, int k) {
    int n = matrix.size();
    priority_queue<int> pq;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            pq.push(-matrix[i][j]);
        }
    }

    for (int i = 1; i < k; i++) {
        pq.pop();
    }

    return -pq.top();
}

int main() {
    vector<vector<int>> matrix = {{1, 5, 9}, {10, 11, 13}, {12, 13, 15}};

    int result = kthSmallest(matrix, 8);

    cout << result << endl;
}