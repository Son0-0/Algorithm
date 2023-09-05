#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;
        vector<double> X(N);
        vector<double> M(N);
        vector<double> ans;

        for (int i = 0; i < N; i++) {
            cin >> X[i];
        }
        for (int i = 0; i < N; i++) {
            cin >> M[i];
        }

        cout << "#" << tc << " ";
        cout << fixed;
        cout.precision(10);

        for (int i = 1; i < N; i++) {
            double low = X[i - 1];
            double high = X[i];
            double mid;
            while (high - low > 1e-12) {
                mid = (low + high) / 2;
                double left = 0.0;
                double right = 0.0;
                for (int i = 0; i < N; i++) {
                    double force = M[i] / ((mid - X[i]) * (mid - X[i]));
                    if (X[i] < mid) {
                        left += force;
                    } else {
                        right += force;
                    }
                }
                if (left < right) {
                    high = mid;
                } else {
                    low = mid;
                }
            }
            ans.push_back(mid);
            cout << mid << " ";
        }
        cout << endl;
    }

    return 0;
}