#include <iostream>
#include <vector>

using namespace std;

bool canBeIncreasing(vector<int>& nums) {
    bool pass = false;
    int prev = nums[0];

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] <= prev) {
            if (pass) {
                return false;
            }

            pass = true;

            if (i == 1 || nums[i - 2] < nums[i]) {
                prev = nums[i];
            }
        } else {
            prev = nums[i];
        }
    }

    return true;
}

int main() {
    vector<int> nums = {1, 2, 10, 5, 7};
    bool result = canBeIncreasing(nums);

    cout << result << endl;
}