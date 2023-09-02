#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

string reorganizeString(string s) {
    unordered_map<char, int> um;

    for (auto c : s) {
        um[c]++;

        if ((s.size() + 1) / 2 < um[c]) {
            return "";
        }
    }

    priority_queue<pair<int, char>> pq;

    for (auto item : um) {
        pq.push(make_pair(item.second, item.first));
    }

    string result = "";
    while (2 <= pq.size()) {
        auto a = pq.top();
        pq.pop();

        auto b = pq.top();
        pq.pop();

        result += a.second;
        result += b.second;

        if (a.first - 1 != 0) {
            pq.push(make_pair(a.first - 1, a.second));
        }

        if (b.first - 1 != 0) {
            pq.push(make_pair(b.first - 1, b.second));
        }
    }

    if (!pq.empty()) {
        result += pq.top().second;
    }

    return result;
}

int main() { cout << reorganizeString("aab") << endl; }