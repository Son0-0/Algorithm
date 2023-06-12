#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> summaryRanges(vector<int>& nums) {
    vector<string> result;

    if (nums.size() == 0) {
        return result;
    }

    int cur = nums[0];
    bool tf = false;

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == nums[i - 1] + 1) {
            tf = true;
        } else {
            if (tf) {
                result.push_back(to_string(cur) + "->" + to_string(nums[i - 1]));
            } else {
                result.push_back(to_string(cur));
            }
            cur = nums[i];
            tf = false;
        }
    }

    // Handle the last range separately
    if (tf) {
        result.push_back(to_string(cur) + "->" + to_string(nums[nums.size() - 1]));
    } else {
        result.push_back(to_string(cur));
    }

    return result;
}

int main() {
    std::vector<int> nums = {0, 1, 2, 4, 5, 7};
    std::vector<std::string> result = summaryRanges(nums);

    std::cout << "Summary Ranges:" << std::endl;
    for (const auto& range : result) {
        std::cout << range << std::endl;
    }

    return 0;
}
