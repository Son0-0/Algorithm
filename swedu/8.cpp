#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    for (int test_case = 1; test_case <= 10; ++test_case) {
        int answer = 0;

        int length = 0;
        scanf("%d", &length);

        if (length == 1) {
            answer = 64;
        } else {
            char map[8][9];

            for (int i = 0; i < 8; i++) {
                scanf("%s", map[i]);
            }

            int last = 8 - length;
            int compare = (8 - length) / 2;
            bool flag = false;

            for (int i = 0; i < 8; i++) {
                for (int j = 0; j <= last; j++) {
                    // row
                    flag = true;
                    for (int k = 0; k < compare; k++) {
                        if (map[i][j + k] != map[i][j + length - 1 - k]) {
                            flag = false;
                            break;
                        }
                    }

                    if (flag) {
                        answer++;
                    }

                    // col
                    flag = true;
                    for (int k = 0; k < compare; k++) {
                        if (map[j + k][i] != map[j + length - 1 - k][i]) {
                            flag = false;
                            break;
                        }
                    }

                    if (flag) {
                        answer++;
                    }
                }
            }
        }

        cout << "#" << test_case << " " << answer << endl;
    }
    return 0;
}