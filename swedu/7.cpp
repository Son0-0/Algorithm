#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    for (int test_case = 1; test_case <= 10; ++test_case) {
        char search[11];
        char target[1001];
        int tc = 0;

        scanf("%d", &tc);
        scanf("%s", search);
        scanf("%s", target);

        int len = 0;
        for (int i = 0; search[i] != '\0'; i++) {
            len++;
        }

        char first = search[0];
        int ans = 0;
        bool flag = false;

        for (int i = 0; target[i] != '\0'; i++) {
            if (target[i] == first) {
                flag = true;
                for (int j = 1; j < len; j++) {
                    if (target[i + j] != search[j]) {
                        flag = false;
                        break;
                    }
                }

                if (flag) {
                    ans++;
                }
            }
        }

        cout << "#" << tc << " " << ans << endl;
    }
    return 0;
}