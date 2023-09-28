#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

const int MAX_NUM = 1000000;
bool isPrime[MAX_NUM + 1];
int eulerPi[MAX_NUM + 1];
long long sum[MAX_NUM + 1];

void makePrime() {
    memset(isPrime, true, sizeof(isPrime));

    for (int i = 2; i <= MAX_NUM; i++) {
        isPrime[i] = true;
    }

    for (int i = 2; i <= sqrt(MAX_NUM); i++) {
        if (!isPrime[i]) continue;

        for (int j = i * 2; j <= MAX_NUM; j += i) {
            isPrime[j] = false;
        }
    }
}

void makeEuler() {
    eulerPi[0] = 0;

    for (int i = 1; i <= MAX_NUM; i++) {
        eulerPi[i] = i;
    }

    for (int i = 2; i <= MAX_NUM; i++) {
        if (isPrime[i]) {
            for (int j = 1; i * j <= MAX_NUM; j++) {
                eulerPi[i * j] = eulerPi[i * j] - (eulerPi[i * j] / i);
            }
        }
    }
}

void makeSum() {
    sum[0] = 0;
    sum[1] = 1;

    for (int i = 2; i <= MAX_NUM; i++) {
        sum[i] = sum[i - 1] + eulerPi[i];
    }
}

int main() {
    makePrime();
    makeEuler();
    makeSum();

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int A, B;
        cin >> A >> B;
        cout << "#" << tc << " " << (sum[B] - sum[A - 1]) << endl;
    }

    return 0;
}