#include <iostream>
#include <set>
#include <vector>
using namespace std;

bool checkValid(vector<vector<int>> &matrix) {
  int size = matrix.size();

  for (int i = 0; i < size; i++) {
    set<int> row, col;

    for (int j = 0; j < size; j++) {
      row.insert(matrix[i][j]);
      col.insert(matrix[j][i]);
    }

    if (row.size() != size || col.size() != size) {
      return false;
    }
  }

  return true;
}

int main() {
  vector<vector<int>> nums{{1, 2, 3}, {3, 1, 2}, {2, 3, 1}};
  int result = checkValid(nums);
  cout << result;
}