#include <algorithm>
#include <vector>

constexpr int MAX = 200001;

using namespace std;

typedef long long ll;

struct Elem {
    ll first, second;
    int idx;
};

Elem arr[MAX];

bool comp(const Elem& a, const Elem& b) {
    return b.second * (a.first - 1) > a.second * (b.first - 1);
}

extern int CalcFinalSpeed(int N, int* a, int* b, int* p);

int MinRailSpeed(int N, int* a, int* b) {
    for (int i = 0; i < N; i++) {
        arr[i] = {a[i], b[i], i};
    }

    sort(arr, arr + N, comp);

    int p[MAX];
    for (int i = 0; i < N; i++) {
        p[i] = arr[i].idx;
    }

    return CalcFinalSpeed(N, a, b, p);
}