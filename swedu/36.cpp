#include <bits/stdc++.h>

using namespace std;

struct Point {
    int x, y;
};

long dist(Point &p, Point &q) {
    return (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y);
}

struct Comp {
    bool comp_in_x;
    Comp(bool b) : comp_in_x(b) {}
    bool operator()(Point &p, Point &q) {
        return (this->comp_in_x ? p.x < q.x : p.y < q.y);
    }
};

long closest_pair(vector<Point>::iterator it, int n) {
    if (n == 2) return dist(it[0], it[1]);
    if (n == 3)
        return min(
            {dist(it[0], it[1]), dist(it[1], it[2]), dist(it[2], it[0])});

    int line = (it[n / 2 - 1].x + it[n / 2].x) / 2;
    long d = min(closest_pair(it, n / 2), closest_pair(it + n / 2, n - n / 2));

    vector<Point> mid;
    mid.reserve(n);

    for (int i = 0; i < n; i++) {
        int t = line - it[i].x;
        if (t * t < d) mid.push_back(it[i]);
    }

    sort(mid.begin(), mid.end(), Comp(false));

    int mid_sz = mid.size();
    for (int i = 0; i < mid_sz - 1; i++)
        for (int j = i + 1;
             j < mid_sz && (mid[j].y - mid[i].y) * (mid[j].y - mid[i].y) < d;
             j++)
            d = min(d, dist(mid[i], mid[j]));

    return d;
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int n;
        cin >> n;

        vector<Point> points(n);
        for (auto it = points.begin(); it != points.end(); it++)
            cin >> it->x >> it->y;

        sort(points.begin(), points.end(), Comp(true));

        cout << "#" << tc << " " << closest_pair(points.begin(), n) << endl;
    }

    return 0;
}