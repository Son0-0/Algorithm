#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string nums;
int cnt, n;
int answer = 0;
vector<vector<int>> memo;

void dfs(int cur) {
    if (cur == cnt) {
        int _sum = stoi(nums);
        if (_sum > answer) {
            answer = _sum;
        }
        return;
    }

    if (memo[cur][stoi(nums)] != -1) {
        return;
    }

    memo[cur][stoi(nums)] = answer;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            char tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;

            dfs(cur + 1);

            tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
    }
}

int main(int argc, char** argv) {
    int test_case;
    int T;

    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case) {
        answer = 0;
        cin >> nums >> cnt;

        n = nums.size();

        memo.clear();
        for (int i = 0; i < cnt; i++) {
            memo.push_back(vector<int>(1000000, -1));
        }

        dfs(0);

        cout << "#" << test_case << " " << answer << endl;
    }
    return 0;