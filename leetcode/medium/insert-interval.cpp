#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals,
                           vector<int>& newInterval) {
    vector<vector<int>> result;
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq(
        intervals.begin(), intervals.end());

    pq.push(newInterval);

    while (!pq.empty()) {
        auto cur = pq.top();
        pq.pop();

        if (result.empty()) {
            result.emplace_back(cur);
        } else {
            auto pos = result.size() - 1;
            auto prev = result.back();

            auto start = cur[0];
            auto end = cur[1];

            if (start <= prev[1]) {
                result[pos][0] = min(start, prev[0]);
                result[pos][1] = max(end, prev[1]);
            } else {
                result.emplace_back(cur);
            }
        }
    }

    return result;
}

int main() {
    vector<vector<int>> interval = {{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}};
    vector<int> newInterval = {2, 5};

    vector<vector<int>> result = insert(interval, newInterval);

    for (auto item : result) {
        cout << item[0] << " " << item[1] << endl;
    }
}