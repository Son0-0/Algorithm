#include <cmath>
#include <iostream>

using namespace std;

typedef long long ll;

int main(int argc, char** argv) {
    int T = 0;
    scanf("%d", &T);

    for (int test_case = 1; test_case <= T; ++test_case) {
        int n, p;
        scanf("%d %d", &n, &p);

        int target = n / p;
        ll answer = 0;

        if (n % p == 0) {
            answer = pow(target, p);
        } else {
            answer = pow(target + 1, n % p) * pow(target, p - n % p);
        }

        printf("#%d %lld\n", test_case, answer);
    }
    return 0;
}