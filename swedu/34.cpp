#include <cstring>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; ++test_case) {
        string s;
        cin >> s;

        int length = s.size();
        vector<int> fail(length, 0);

        for (int i = 1, j = 0; i < length; i++) {
            while (j > 0 && s[i] != s[j]) {
                j = fail[j - 1];
            }

            if (s[i] == s[j]) fail[i] = ++j;
        }

        printf("#%d ", test_case);
        int val = fail[length - 1];
        if ((length % (length - val)))
            puts("1");
        else
            printf("%d\n", length / (length - val));
    }
    return 0;
}