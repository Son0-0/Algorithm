#include <iostream>
#include <vector>

using namespace std;

int findMaxConsecutiveOnes(vector<int>& nums) {
    int result = 0;
    int cnt = 0;
    for (auto num : nums) {
        if (num == 1) {
            cnt++;
        } else {
            cnt = 0;
        }

        if (result < cnt) {
            result = cnt;
        }
    }

    return result;
}

int main() {
    vector<int> nums = {1, 1, 0, 1, 1, 1};
    int result = findMaxConsecutiveOnes(nums);
    cout << result << endl;
}