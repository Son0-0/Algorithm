#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dp[100];

int rob(vector<int>& nums) {
    int length = nums.size();

    if (length == 0) {
        return 0;
    } else if (length == 1) {
        return nums[0];
    } else if (length == 2) {
        return max(nums[0], nums[1]);
    }

    int result = 0;

    dp[0] = nums[0];
    dp[1] = nums[1];
    dp[2] = nums[0] + nums[2];

    for (int i = 0; i < length; i++) {
        if (i < 3) {
            result = max(result, dp[i]);
        } else {
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3]);
            result = max(result, dp[i]);
        }
    }

    return result;
}

int main() {
    vector<int> nums = {2, 7, 9, 3, 1};
    int result = rob(nums);
    cout << "resultL: " << result << endl;
}