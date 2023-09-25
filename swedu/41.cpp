#include <cstring>
#include <iostream>

#define MAX_NODE 501

using namespace std;

int n, m;
int dist[MAX_NODE][MAX_NODE];

int main(int argc, char** argv) {
    int T;
    scanf("%d", &T);
    for (int test_case = 1; test_case <= T; ++test_case) {
        scanf("%d %d", &n, &m);

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j)
                    dist[i][j] = 0;
                else
                    dist[i][j] = 1e9;
            }
        }

        int a, b, c;
        for (int i = 0; i < m; i++) {
            scanf("%d %d %d", &a, &b, &c);
            if (c < dist[a][b]) dist[a][b] = c;
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        printf("#%d ", test_case);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (dist[i][j] >= 1e9)
                    printf("-1 ");
                else
                    printf("%d ", dist[i][j]);
            }
        }
        puts("");
    }
    return 0;
}