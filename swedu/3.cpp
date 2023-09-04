#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int comb[19][19];

void combination() {
    for (int i = 1; i < 19; i++) {
        comb[i][0] = 1;
        comb[i][i] = 1;
    }

    for (int i = 2; i < 19; i++) {
        for (int j = 1; j < i; j++) {
            // nCr = n-1Cr-1 + n-1Cr
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
        }
    }
}

double calculatePercentage(int percent, int num) {
    return pow(percent / 100.0, num) * pow((100.0 - percent) / 100.0, 18 - num);
}

int main(int argc, char** argv) {
    int test_case;
    int T;
    int notPrime[12] = {0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18};
    combination();

    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case) {
        int masterA, masterB;

        scanf("%d %d\n", &masterA, &masterB);

        double percentA = 0.0;
        double percentB = 0.0;

        for (int i = 0; i < 12; i++) {
            int notPrimeNum = notPrime[i];
            // 18개 중에 소수개 만들 확률
            double pA = calculatePercentage(masterA, notPrimeNum);
            double pB = calculatePercentage(masterB, notPrimeNum);

            int combNum = comb[18][notPrimeNum];

            percentA += combNum * pA;
            percentB += combNum * pB;
        }

        printf("#%d %.6f\n", test_case, 1 - (percentA * percentB));
    }
    return 0;
}