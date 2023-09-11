#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int N;
int idx;
int Firstchild[101], Secondchild[101];
char Alpha[101];
char Answer[101];

void inorder(int cur) {
    if (Alpha[cur] == 0) {
        return;
    }

    inorder(Firstchild[cur]);
    Answer[idx++] = Alpha[cur];
    inorder(Secondchild[cur]);
}

int main(int argc, char** argv) {
    int test_case;

    for (test_case = 1; test_case <= 10; ++test_case) {
        int i;
        memset(Firstchild, 0, sizeof(int) * 101);
        memset(Secondchild, 0, sizeof(int) * 101);
        memset(Alpha, 0, sizeof(char) * 101);
        memset(Answer, 0, sizeof(char) * 101);

        cin >> N;
        idx = 0;
        for (i = 0; i < N; i++) {
            int addr;
            char buf[100];

            cin >> addr;
            cin >> buf;

            Alpha[addr] = buf[0];

            if (addr * 2 <= N) {
                cin >> Firstchild[addr];
                if (addr * 2 + 1 <= N) scanf("%d ", &Secondchild[addr]);
            }
        }

        inorder(1);

        cout << "#" << test_case << " ";

        for (int i = 0; i < N; i++) {
            cout << Answer[i];
        }
        cout << endl;
    }

    return 0;
}