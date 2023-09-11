#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int N;
int Number[1001], Firstchild[1001], Secondchild[1001];
char Operator[1001];

int inorder(int cur) {
    if (!Operator[cur]) return Number[cur];

    int left, right;
    left = inorder(Firstchild[cur]);
    right = inorder(Secondchild[cur]);

    char op = Operator[cur];
    if (op == '+')
        return left + right;
    else if (op == '-')
        return left - right;
    else if (op == '/')
        return left / right;
    else
        return left * right;
}

int main(int argc, char** argv) {
    int test_case;

    for (test_case = 1; test_case <= 10; ++test_case) {
        int i;
        memset(Firstchild, 0, sizeof(int) * 1001);
        memset(Secondchild, 0, sizeof(int) * 1001);
        memset(Number, 0, sizeof(int) * 1001);
        memset(Operator, 0, sizeof(char) * 1001);

        cin >> N;
        for (i = 0; i < N; i++) {
            int addr;
            char buf[100];

            cin >> addr;
            cin >> buf;
            if ((buf[0] == '+') || (buf[0] == '-') || (buf[0] == '*') ||
                (buf[0] == '/')) {
                Operator[addr] = buf[0];
                cin >> Firstchild[addr] >> Secondchild[addr];
            } else
                Number[addr] = atoi(buf);
        }

        int answer = 0;
        answer = inorder(1);

        cout << "#" << test_case << " " << answer << endl;
    }

    return 0;
}