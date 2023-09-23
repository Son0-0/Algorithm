#include <cstring>
#include <iostream>
#include <string>

constexpr int MAX = 1001;

using namespace std;

int lcs[MAX][MAX];

int main(int argc, char** argv) {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        string a, b;
        cin >> a >> b;

        a = "0" + a;
        b = "0" + b;

        memset(lcs, 0, sizeof(lcs));

        int lenA = a.size();
        int lenB = b.size();
        int ans = 0;
        for (int i = 0; i < lenA; i++) {
            for (int j = 0; j < lenB; j++) {
                if (i == 0 || j == 0) {
                    lcs[i][j] = 0;
                    continue;
                }

                if (a[i] == b[j]) {
                    lcs[i][j] = lcs[i - 1][j - 1] + 1;
                } else {
                    int aa = lcs[i - 1][j];
                    int bb = lcs[i][j - 1];

                    lcs[i][j] = aa > bb ? aa : bb;
                }
            }
        }

        printf("#%d %d\n", tc, lcs[lenA - 1][lenB - 1]);
    }
    return 0;
}