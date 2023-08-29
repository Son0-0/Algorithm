#include <iostream>
#include <vector>

using namespace std;

int count = 0;

void dfs(int cur, vector<int> &visited, vector<int> &nums) {
    if (visited.size() == 4) {
        if (nums[visited[0]] + nums[visited[1]] + nums[visited[2]] ==
            nums[visited[3]]) {
            count++;
        }
        return;
    }

    for (int i = cur + 1; i < nums.size(); i++) {
        visited.push_back(i);
        dfs(i, visited, nums);
        visited.pop_back();
    }
}

int countQuadruplets(vector<int> &nums) {
    vector<int> visited;
    dfs(-1, visited, nums);
    return count;
}

int main() {
    vector<int> nums = {1, 1, 1, 3, 5};
    cout << countQuadruplets(nums) << endl;
}