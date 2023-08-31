#include <iostream>
#include <vector>

using namespace std;

int max(int a, int b) {
    if (a < b) {
        return b;
    }
    return a;
}

int maxAscendingSum(vector<int>& nums) {
    int sum = nums[0];
    int prev = nums[0];
    int result = sum;

    for (int i = 1; i < nums.size(); i++) {
        if (prev < nums[i]) {
            sum += nums[i];
        } else if (prev >= nums[i]) {
            sum = nums[i];
        }

        prev = nums[i];
        result = max(result, sum);
    }

    return result;
}

int main() {
    vector<int> nums = {12, 17, 15, 13, 10, 11, 12};
    cout << maxAscendingSum(nums) << endl;
}