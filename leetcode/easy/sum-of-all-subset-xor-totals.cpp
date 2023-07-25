#include <iostream>
#include <vector>

using namespace std;

int result = 0;

void dfs(vector<int>& nums, int index, int curValue) {
    for (int i = index + 1; i < nums.size(); i++) {
        result += curValue ^ nums[i];
        dfs(nums, i, curValue ^ nums[i]);
    }
}

int subsetXORSum(vector<int>& nums) { dfs(nums, -1, 0); }

int main() {
    vector<int> nums = {5, 1, 6};
    int result = subsetXORSum(nums);

    cout << result << endl;
}