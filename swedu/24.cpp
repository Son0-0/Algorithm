#include <iostream>
#include <queue>
#include <vector>

#define MAX 50001

using namespace std;

int indegree[MAX];
vector<int> students[MAX];

int main(int argc, char** argv) {
    int T;
    scanf("%d", &T);

    for (int test_case = 1; test_case <= T; ++test_case) {
        int n, m;
        scanf("%d %d", &n, &m);

        for (int i = 1; i <= n; i++) {
            students[i].clear();
            indegree[i] = 0;
        }

        int a, b;
        for (int i = 0; i < m; i++) {
            scanf("%d %d", &a, &b);
            indegree[b]++;
            students[a].push_back(b);
        }

        queue<int> q;
        for (int i = 1; i <= n; i++) {
            if (!indegree[i]) {
                q.push(i);
            }
        }

        printf("#%d", test_case);
        vector<int> result;
        while (!q.empty()) {
            int cur = q.front();
            q.pop();

            printf(" %d", cur);

            for (auto node : students[cur]) {
                indegree[node]--;

                if (!indegree[node]) {
                    q.push(node);
                }
            }
        }

        puts("");
    }
    return 0;
}