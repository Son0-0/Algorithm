#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int N;
int Firstchild[201], Secondchild[201], Num[201];
char Oper[201];

int main(int argc, char** argv) {
    int test_case;

    for (test_case = 1; test_case <= 10; ++test_case) {
        int i;
        memset(Firstchild, 0, sizeof(int) * 201);
        memset(Secondchild, 0, sizeof(int) * 201);
        memset(Num, 0, sizeof(int) * 201);
        memset(Oper, 0, sizeof(char) * 201);

        cin >> N;

        int answer = 1;
        for (i = 1; i <= N; i++) {
            char ch;
            cin >> i >> ch;

            if (i <= N / 2) {
                int left, right;

                if (i == N / 2 && N % 2 == 0)
                    cin >> left;
                else
                    cin >> left >> right;

                if (ch >= '0' && ch <= '9') answer = 0;
            } else {
                if (!(ch >= '0' && ch <= '9')) answer = 0;
            }
        }

        cout << "#" << test_case << " " << answer << endl;
    }

    return 0;
}