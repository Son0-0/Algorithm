#include <iostream>
#include <vector>
using namespace std;

int abs(int target) {
  if (0 < target) {
    return target;
  }
  return -target;
}

int check(int target) {
  int count = 0;

  while (target >= 10) {
    target /= 10;
    count++;
  }

  return count + 1;
}

int findNumbers(vector<int> &nums) {
  int count = 0;

  for (int i = 0; i < nums.size(); i++) {
    if (check(nums[i]) % 2 == 0) {
      count++;
    }
  }

  return count;
}

int main() {
  vector<int> nums{12, 345, 2, 6, 7896};
  int result = findNumbers(nums);

  cout << result;
}