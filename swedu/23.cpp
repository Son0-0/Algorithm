#include <algorithm>
#include <iostream>

using namespace std;

typedef long long ll;

constexpr int MAX_ELEM = 11;

struct Elem {
    int first;
    int second;
};

Elem arr[MAX_ELEM];

int main(int argc, char** argv) {
    int T;
    scanf("%d", &T);
    for (int test_case = 1; test_case <= T; ++test_case) {
        int N;
        scanf("%d", &N);

        int M = 1;
        for (int i = 0; i < N; i++) {
            scanf("%d %d", &arr[i].first, &arr[i].second);
            M *= arr[i].second;
        }

        ll sum = 0;
        for (int i = 0; i < N; i++) {
            ll m = M / arr[i].second;
            ll rm = 0;
            for (int j = 1; j <= 4000; j++) {
                if ((m * j) % arr[i].second == 1) {
                    rm = j;
                    break;
                }
            }

            sum += (m * rm * arr[i].first);
        }

        printf("#%d %d\n", test_case, sum % M);
    }
    return 0;
}