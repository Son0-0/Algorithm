#include <climits>
#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

#define MAX_CITY 200001
#define INF LLONG_MAX

using namespace std;

typedef long long ll;
typedef pair<ll, int> PAIR;
typedef priority_queue<PAIR, vector<PAIR>, greater<PAIR>> pq;

struct Node {
    int id;
    ll cost;
    bool checked;

    Node(int a, int b, bool c) : id(a), cost(b), checked(c) {}
};

int n, m;
vector<Node> graph[MAX_CITY];
bool visited[MAX_CITY];
ll dist[MAX_CITY];
int rt[MAX_CITY];
ll answer;

Node& getNode(int a, int b) {
    for (Node& node : graph[a]) {
        if (node.id == b) {
            return node;
        }
    }

    static Node dummy = {-1, -1, false};
    return dummy;
}

void calc() {
    for (int i = 2; i <= n; i++) {
        for (int prev = i; prev != 1; prev = rt[prev]) {
            int a = prev;
            int b = rt[prev];
            Node& node = getNode(a, b);

            if (node.checked) break;

            answer += node.cost;
            node.checked = true;

            Node& node2 = getNode(b, a);
            node2.checked = true;
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        scanf("%d %d", &n, &m);

        // initialize
        for (int i = 1; i <= n; i++) {
            graph[i].clear();
            visited[i] = false;
            dist[i] = INF;
            rt[i] = -1;
        }

        int s, e, d;
        for (int i = 0; i < m; i++) {
            scanf("%d %d %d", &s, &e, &d);
            graph[s].emplace_back(e, d, false);
            graph[e].emplace_back(s, d, false);
        }

        answer = 0;
        pq q;
        q.push({0, 1});
        dist[1] = 0;
        rt[1] = 1;

        while (!q.empty()) {
            auto& cur = q.top();
            ll dis = cur.first;
            int pos = cur.second;
            q.pop();

            if (visited[pos]) continue;

            visited[pos] = true;

            for (auto& node : graph[pos]) {
                if (dis + node.cost <= dist[node.id]) {
                    dist[node.id] = dis + node.cost;

                    if (rt[node.id] == -1) {
                        rt[node.id] = pos;
                    } else {
                        auto a = getNode(pos, node.id);
                        auto b = getNode(rt[node.id], node.id);

                        if (a.cost < b.cost) {
                            rt[node.id] = pos;
                        }
                    }

                    q.push({dist[node.id], node.id});
                }
            }
        }

        calc();

        printf("#%d %lld\n", tc, answer);
    }
}