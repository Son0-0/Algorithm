#include <iostream>
#include <vector>
using namespace std;

int findKthPositive(vector<int> &arr, int k) {
  for (int i = 0; i < arr.size(); i++) {
    if (k <= arr[i] - i - 1) {
      return i + k;
    }
  }
  return k + arr.size();
}

int main() {
  vector<int> nums{2, 3, 4, 7, 11};
  int result = findKthPositive(nums, 5);

  cout << result;
}