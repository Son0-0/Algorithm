include<memory.h>

    int Fail[500001];

int FindString(int N, char *H, int M, char *S) {
    memset(Fail, 0, sizeof(int) * M);

    int begin = 1, m = 0;
    while (begin + m < M) {
        if (S[begin + m] == S[m]) {
            m++;
            Fail[begin + m - 1] = m;
        } else {
            if (m == 0)
                begin++;
            else {
                begin += (m - Fail[m - 1]);
                m = Fail[m - 1];
            }
        }
    }

    int cnt = 0;
    begin = 0;
    m = 0;
    while (begin <= N - M) {
        if (m < M && H[begin + m] == S[m]) {
            m++;
            if (m == M) cnt++;
        } else {
            if (m == 0)
                begin++;
            else {
                begin += (m - Fail[m - 1]);
                m = Fail[m - 1];
            }
        }
    }

    return cnt;
}