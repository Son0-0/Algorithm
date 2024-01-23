#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int matrixSum(vector<vector<int>>& nums) {
    vector<priority_queue<int>> pq(nums.size());

    for (int i = 0; i < nums.size(); i++) {
        for (auto num : nums[i]) {
            pq[i].push(num);
        }
    }

    int score = 0;
    for (int i = 0; i < nums[0].size(); i++) {
        int temp = 0;
        for (int j = 0; j < nums.size(); j++) {
            temp = max(temp, pq[j].top());
            pq[j].pop();
        }
        score += temp;
    }

    return score;
}

int main() {
    vector<vector<int>> nums = {{7, 2, 1}, {6, 4, 2}, {6, 5, 3}, {3, 2, 1}};

    int result = matrixSum(nums);

    cout << result << endl;
}