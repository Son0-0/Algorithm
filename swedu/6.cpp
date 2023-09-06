#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main() {
    for (int test_case = 1; test_case <= 10; test_case++) {
        int N;
        cin >> N;
        vector<vector<int>> map(N, vector<int>(N));

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cin >> map[i][j];
            }
        }

        int cnt = 0;
        for (int j = 0; j < N; j++) {
            int row = 0;
            int col = j;

            stack<int> s;

            while (row < N) {
                if (s.empty() && map[row][col] == 1) {
                    s.push(1);
                } else if (!s.empty() && map[row][col] == 2) {
                    cnt++;
                    s.pop();
                }
                row++;
            }
        }

        cout << "#" << test_case << " " << cnt << endl;
    }

    return 0;
}