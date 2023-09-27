#include <iostream>

using namespace std;

#define MAX 21

typedef long long ll;

ll dp[MAX][MAX][MAX] = {
    0,
};

void init() {
    dp[1][1][1] = 1;

    for (int i = 2; i <= 20; i++) {
        for (int j = 1; j <= 20; j++) {
            for (int k = 1; k <= 20; k++) {
                dp[i][j][k] = dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] +
                              dp[i - 1][j][k] * (i - 2);
            }
        }
    }
}

int main(int argc, char** argv) {
    int T;
    scanf("%d", &T);

    init();
    for (int test_case = 1; test_case <= T; ++test_case) {
        int n, l, r;
        scanf("%d %d %d", &n, &l, &r);
        printf("#%d %lld\n", test_case, dp[n][l][r]);
    }
    return 0;
}