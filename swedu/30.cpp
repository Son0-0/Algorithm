#include <algorithm>
#include <iostream>
#include <queue>

#define MAX_CITY 50001

using namespace std;

typedef pair<int, pair<int, int>> p;
typedef priority_queue<p, vector<p>, greater<p>> pq;

int n, m;
int parent[MAX_CITY];

int find(int target) {
    if (target == parent[target]) return target;
    return parent[target] = find(parent[target]);
}

void unionNode(int x, int y) {
    x = parent[x];
    y = parent[y];

    if (x > y)
        parent[x] = parent[y];
    else
        parent[y] = parent[x];
}

int main(int argc, char** argv) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        cin >> n;
        cin >> m;

        for (int i = 1; i <= n; i++) parent[i] = i;

        int s, e, c;
        pq roads;
        for (int i = 0; i < m; i++) {
            cin >> s >> e >> c;
            roads.push({c, {s, e}});
        }

        int answer = 0;
        int nodeCnt = 0;
        while (!roads.empty()) {
            auto& cur = roads.top();

            int src = cur.second.first;
            int dest = cur.second.second;

            if (find(src) == find(dest)) {
                roads.pop();
                continue;
            }

            unionNode(src, dest);
            answer += cur.first;
            nodeCnt++;
            roads.pop();

            if (nodeCnt == n - 1) break;
        }

        cout << "#" << test_case << " " << answer << endl;
    }
    return 0;
}