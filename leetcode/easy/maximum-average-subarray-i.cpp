#include <iostream>
#include <vector>

using namespace std;

double findMaxAverage(vector<int>& nums, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) {
        sum += nums[i];
    }

    double result = sum / double(k);

    for (int i = k; i < nums.size(); i++) {
        sum += nums[i] - nums[i - k];
        if (result < sum / double(k)) {
            result = sum / double(k);
        }
    }

    return result;
}

int main() {
    vector<int> nums = {1, 12, -5, -6, 50, 3};
    double result = findMaxAverage(nums, 4);

    cout << result << endl;
}