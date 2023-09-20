#include <algorithm>
#include <cstring>
#include <iostream>
#include <set>

#define MAX 501

using namespace std;

struct job {
    int s, e, c;
};

bool comp(job& a, job& b) {
    if (a.e == b.e) return a.s < b.s;
    return a.e < b.e;
}

int dp[MAX];
job jobs[MAX];

int calc(int i) {
    int target = jobs[i].s;
    for (int j = i - 1; j >= 0; j--) {
        if (jobs[j].e < target) {
            return dp[j];
        }
    }
    return 0;
}

int main(int argc, char** argv) {
    int T;
    // freopen("input.txt", "r", stdin);
    cin >> T;
    for (int test_case = 1; test_case <= T; ++test_case) {
        int n, m;

        cin >> n >> m;

        int start, end, cost;
        for (int i = 0; i < n; i++) {
            cin >> start >> end >> cost;
            jobs[i] = {start, end, cost};
        }

        sort(jobs, jobs + n, comp);

        dp[0] = jobs[0].c;

        int idx = 1;
        for (int i = 1; i < n; i++) {
            int target = jobs[i].c + calc(i);
            dp[i] = dp[i - 1] < target ? target : dp[i - 1];
        }

        printf("#%d %d\n", test_case, dp[n - 1]);
    }
    return 0;
}