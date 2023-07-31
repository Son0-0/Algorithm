#include <iostream>
#include <vector>

using namespace std;

bool isPrime(int target) {
    if (target == 1) return false;
    for (int i = 2; i * i <= target; i++) {
        if (target % i == 0) {
            return false;
        }
    }
    return true;
}

int diagonalPrime(vector<vector<int>> &nums) {
    int n = nums.size();
    int result = 0;

    for (int i = 0; i < nums.size(); i++) {
        if (isPrime(nums[i][i])) {
            if (nums[i][i] > result) {
                result = nums[i][i];
            }
        }

        if (isPrime(nums[i][n - 1 - i])) {
            if (nums[i][n - 1 - i] > result) {
                result = nums[i][n - 1 - i];
            }
        }
    }

    return result;
}

int main() {
    vector<vector<int>> nums = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int result = diagonalPrime(nums);
    cout << result << endl;
}