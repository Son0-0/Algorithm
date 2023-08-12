#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int largestSumAfterKNegations(vector<int>& nums, int k) {
    priority_queue<int> pq;

    for (auto num : nums) {
        pq.push(-num);
    }

    while (k > 0) {
        int cur = pq.top();
        pq.pop();
        pq.push(-cur);
        k--;
    }

    int sum = 0;
    while (!pq.empty()) {
        sum += -pq.top();
        pq.pop();
    }

    return sum;
}

int main() {
    vector<int> nums = {4, 2, 3};
    int result = largestSumAfterKNegations(nums, 1);
    cout << result << endl;
}