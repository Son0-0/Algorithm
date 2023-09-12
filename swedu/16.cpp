#include <iostream>

constexpr int MAX_BLOCK = 200001;

using namespace std;

int N, K;
int LENGTH;  // 초기 블록 수
int answer;
int BLOCKS[MAX_BLOCK], INIT[MAX_BLOCK];

bool isPossible(int target) {
    int count = 0;
    int cur = 1;

    for (int i = 1; i <= N; i++) {
        if (BLOCKS[i] <= target)
            count++;
        else
            count = 0;

        if (count == INIT[cur]) {
            cur++;
            count = 0;
            if (cur > K) break;
        }
    }

    return cur > K;
}

int main(int argc, char** argv) {
    int test_case;
    int T;

    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case) {
        cin >> N >> K;

        LENGTH = 0;

        int left = MAX_BLOCK;
        int right = 0;

        for (int i = 1; i <= N; i++) {
            scanf("%d", &BLOCKS[i]);

            if (right < BLOCKS[i]) right = BLOCKS[i];

            if (BLOCKS[i] < left) left = BLOCKS[i];
        }

        for (int i = 1; i <= K; i++) {
            scanf("%d", &INIT[i]);
            LENGTH += INIT[i];
        }

        int mid;
        int answer = 0;

        while (left <= right) {
            mid = (left + right) / 2;

            if (isPossible(mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        printf("#%d %d\n", test_case, answer);
    }
    return 0;
}