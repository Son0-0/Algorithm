#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<int> findErrorNums(vector<int>& nums) {
    vector<int> result;
    map<int, bool> m;

    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size() - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            result.push_back(nums[i]);
        }
        m[nums[i]] = true;
    }
    m[nums[nums.size() - 1]] = true;

    for (int i = 1; i <= nums.size(); i++) {
        if (m.find(i) == m.end()) {
            result.push_back(i);
            break;
        }
    }

    return result;
}

int main() {
    vector<int> nums = {1, 2, 2, 4};

    for (auto num : findErrorNums(nums)) {
        cout << num << " ";
    }
}