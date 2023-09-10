#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    for (int test_case = 1; test_case <= 10; ++test_case) {
        int v, e;  // 정점, 간선
        scanf("%d %d", &v, &e);

        vector<int> topology(v + 1, 0);
        vector<vector<bool>> node;

        node.assign(v + 1, vector<bool>(v + 1, false));

        for (int i = 0; i < e; i++) {
            // a -> b
            int src, dest;
            scanf("%d", &src);
            scanf("%d", &dest);

            topology[dest]++;

            node[src][dest] = true;
        }

        queue<int> q;
        for (int i = 1; i <= v; i++) {
            if (!topology[i]) {
                q.push(i);
            }
        }

        printf("#%d", test_case);

        while (!q.empty()) {
            int cur = q.front();
            q.pop();

            printf(" %d", cur);

            for (int i = 1; i <= v; i++) {
                if (node[cur][i]) {
                    node[cur][i] = false;

                    topology[i]--;

                    if (!topology[i]) {
                        q.push(i);
                    }
                }
            }
        }
        puts("");
    }
    return 0;
}