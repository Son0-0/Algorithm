#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

#define MAX 11

int graph[MAX][MAX] = {
    0,
};
int secret[MAX];
int visited[MAX];
int answer;
int n, k;

void dfs(int cur, int length) {
    if (answer < length) answer = length;

    for (int i = 1; i <= n; i++) {
        if (graph[cur][i] == 1) {
            if (visited[i] == 0) {
                visited[i] = 1;
                dfs(i, length + 1);
                visited[i] = 0;
            }
        }
    }
}

int main(int argc, char** argv) {
    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        cin >> n >> k;

        for (int i = 1; i <= n; i++) {
            memset(graph[i], 0, sizeof(int) * (n + 1));
        }
        answer = 0;

        for (int i = 0; i < k; i++) {
            int num;
            cin >> num;
            for (int i = 0; i < num; i++) {
                cin >> secret[i];
            }

            for (int i = 0; i < num - 1; i++) {
                graph[secret[i]][secret[i + 1]] = 1;
            }
        }

        for (int i = 1; i <= n; i++) {
            memset(visited, 0, sizeof(int) * (n + 1));
            visited[i] = 1;
            dfs(i, 1);
        }

        cout << "#" << test_case << " ";
        for (int i = 1; i <= n; i++) {
            int cnt = 0;
            for (int j = 1; j <= n; j++) {
                if (graph[i][j] == 1) cnt++;
            }
            cout << cnt << " ";
        }
        cout << answer << endl;
    }
    return 0;
}