#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int max(int a, int b) {
    if (a < b) {
        return b;
    }
    return a;
}

int main(int argc, char** argv) {
    int test_case;
    int T;

    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case) {
        int size = 0;
        string str;

        scanf("%d\n", &size);
        getline(cin, str);

        vector<int> nums;

        stringstream orgNum(str);
        int newNum;

        while (orgNum >> newNum) {
            nums.push_back(newNum);
        }

        int ans = 0;
        for (int i = nums.size() - 2; i >= 2; i--) {
            int left = max(nums[i - 2], nums[i - 1]);
            int right = max(nums[i + 1], nums[i + 2]);

            int target = nums[i] - max(left, right);

            if (0 < target) {
                ans += target;
            }
        }

        cout << "#" << test_case << " " << ans << endl;
    }
    return 0;
}