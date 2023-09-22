#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

constexpr int MAX_POINT = 10001;

using namespace std;

typedef long long ll;

struct Node {
    ll x;
    ll y;
};

bool cmp(const Node &a, const Node &b) {
    if (a.x != b.x) {
        return a.x < b.x;
    }

    if (a.y != b.y) {
        return a.y < b.y;
    }

    return true;
}

Node Points[MAX_POINT];

ll ccw(const Node &a, const Node &b, const Node &c) {
    return a.x * b.y + b.x * c.y + c.x * a.y - b.x * a.y - c.x * b.y -
           a.x * c.y;
}

int main(int argc, char **argv) {
    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; ++test_case) {
        int n, e;
        cin >> n >> e;

        ll a, b;
        for (int i = 0; i < n; i++) {
            cin >> a >> b;
            Points[i] = {a, b};
        }

        sort(Points, Points + n, cmp);

        vector<ll> dp(n + 1, LLONG_MAX);
        dp[0] = 0;

        for (int i = 0; i < n - 1; i++) {
            Node og = Points[i];
            Node U = {Points[i + 1].x, Points[i + 1].y + e};
            Node L = {Points[i + 1].x, Points[i + 1].y - e};

            if (dp[i + 1] > dp[i]) dp[i + 1] = dp[i] + 1;

            for (int j = i + 2; j < n; j++) {
                Node tempU = {Points[j].x, Points[j].y + e};
                Node tempL = {Points[j].x, Points[j].y - e};

                if (ccw(og, U, tempU) < 0) {
                    U = tempU;
                }

                if (ccw(og, L, tempL) > 0) {
                    L = tempL;
                }

                if (ccw(og, U, L) > 0) {
                    break;
                }

                if (ccw(og, L, Points[j]) >= 0 && ccw(og, U, Points[j]) <= 0) {
                    if (dp[j] > dp[i] + 1) {
                        dp[j] = dp[i] + 1;
                    }
                }
            }
        }

        printf("#%d %lld\n", test_case, dp[n - 1]);
    }
    return 0;
}