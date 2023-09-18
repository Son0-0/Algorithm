// convex hull algorithm
#include <algorithm>
#include <iostream>

#define MAX 100002

using namespace std;

typedef long long ll;

struct Node {
    ll x, y;

    bool operator<(const Node &a) { return y == a.y ? x < a.x : y < a.y; }
};

Node p[MAX];
int stack[MAX];
int top;

ll ccw(const Node &a, const Node &b, const Node &c) {
    return a.x * b.y + b.x * c.y + c.x * a.y - b.x * a.y - c.x * b.y -
           a.x * c.y;
}

ll dist(Node a, Node b) {
    return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

bool cmp(const Node &a, const Node &b) {
    ll c = ccw(p[0], a, b);
    if (c == 0) {
        return dist(p[0], a) < dist(p[0], b);
    }
    return c > 0;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        top = 0;
        int n;
        scanf("%d", &n);

        int x, y;
        for (int i = 0; i < n; i++) {
            scanf("%lld %lld", &p[i].x, &p[i].y);
        }

        sort(p, p + n);
        sort(p + 1, p + n, cmp);

        stack[top++] = 0;
        stack[top++] = 1;

        for (int i = 2; i < n; i++) {
            while (top >= 2 &&
                   ccw(p[i], p[stack[top - 2]], p[stack[top - 1]]) <= 0)
                top--;
            stack[top++] = i;
        }

        printf("#%d %d\n", tc, top);
    }
    return 0;
}