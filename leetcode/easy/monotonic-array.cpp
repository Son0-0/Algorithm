#include <iostream>
#include <vector>

using namespace std;

bool isMonotonic(vector<int>& nums) {
    bool increase = false;
    bool decrease = false;

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] - nums[i - 1] > 0) {
            increase = true;
        }

        if (nums[i] - nums[i - 1] < 0) {
            decrease = true;
        }

        if (increase && decrease) {
            return false;
        }
    }

    return true;
}

int main() {
    vector<int> nums = {1, 2, 2, 3};

    bool result = isMonotonic(nums);

    cout << result << endl;
}