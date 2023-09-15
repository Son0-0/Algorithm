
#include <iostream>
#include <queue>
#include <vector>

#define MAX_E 50001

using namespace std;

typedef pair<int, int> PAIR;
typedef priority_queue<PAIR, vector<PAIR>, greater<PAIR>> pq;

vector<PAIR> in[MAX_E];
vector<PAIR> out[MAX_E];

int main(int argc, char** argv) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        int n, m, x;
        cin >> n >> m >> x;

        for (int i = 1; i <= n; i++) {
            in[i].clear();
            out[i].clear();
        }

        int s, e, t;
        for (int i = 0; i < m; i++) {
            cin >> s >> e >> t;
            in[e].push_back({s, t});
            out[s].push_back({e, t});
        }

        vector<int> inDis(n + 1, 1e9);
        vector<int> outDis(n + 1, 1e9);

        inDis[x] = 0;
        outDis[x] = 0;

        pq q;
        q.emplace(0, x);

        while (!q.empty()) {
            auto& cur = q.top();
            int dis = cur.first;
            int pos = cur.second;
            q.pop();

            if (inDis[pos] < dis) continue;

            for (auto& node : in[pos]) {
                if (dis + node.second < inDis[node.first]) {
                    inDis[node.first] = dis + node.second;
                    q.emplace(dis + node.second, node.first);
                }
            }
        }

        q = pq();
        q.emplace(0, x);

        int answer = 0;
        while (!q.empty()) {
            auto& cur = q.top();
            int dis = cur.first;
            int pos = cur.second;
            q.pop();

            if (outDis[pos] < dis) continue;

            if (answer < inDis[pos] + outDis[pos])
                answer = inDis[pos] + outDis[pos];

            for (auto& node : out[pos]) {
                if (dis + node.second < outDis[node.first]) {
                    outDis[node.first] = dis + node.second;
                    q.emplace(dis + node.second, node.first);
                }
            }
        }

        cout << "#" << test_case << " " << answer << endl;
    }
    return 0;
}