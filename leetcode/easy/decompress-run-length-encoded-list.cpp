#include <iostream>
#include <vector>

using namespace std;

vector<int> decompressRLElist(vector<int>& nums) {
    vector<int> result;

    for (int i = 0; i < nums.size(); i += 2) {
        for (int freq = 0; freq < nums[i]; freq++) {
            result.push_back(nums[i + 1]);
        }
    }

    return result;
}

int main() {
    vector<int> nums = {1, 2, 3, 4};
    vector<int> result = decompressRLElist(nums);

    for (auto key : result) {
        cout << key << " ";
    }
    cout << endl;
}