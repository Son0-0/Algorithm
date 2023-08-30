#include <iostream>
#include <vector>

using namespace std;

int abs(int target) {
    if (target < 0) {
        return -target;
    }
    return target;
}

int findClosestNumber(vector<int>& nums) {
    pair<int, int> p(abs(nums[0]), nums[0]);

    for (auto num : nums) {
        if (abs(num) < p.first) {
            p = make_pair(abs(num), num);
        } else if (abs(num) == p.first) {
            if (p.second < num) {
                p = make_pair(abs(num), num);
            }
        }
    }

    return p.second;
}

int main() {
    vector<int> nums = {-4, -2, 1, 4, 8};
    cout << findClosestNumber() << endl;
}