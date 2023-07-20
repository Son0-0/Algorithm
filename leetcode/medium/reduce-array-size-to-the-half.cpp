#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

int minSetSize(vector<int> &arr) {
    map<int, int> m;

    for (auto num : arr) {
        m[num]++;
    }

    int size = arr.size();
    int cur = size;

    size /= 2;

    priority_queue<pair<int, int>> pq;
    for (const auto &item : m) {
        pq.push({item.second, item.first});
    }

    int cnt = 0;
    while (cur > size) {
        cur -= pq.top().first;
        pq.pop();
        cnt++;
    }

    return cnt;
}

int main() {
    vector<int> nums{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int result = minSetSize(nums);

    cout << result << "\n";
}