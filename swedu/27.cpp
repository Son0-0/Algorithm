#include <cstring>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> jokbos = {"Top",        "1 Pair",   "2 Pair",
                         "Triple",     "Straight", "Flush",
                         "Full House", "4 Card",   "Straight Flush"};

struct card {
    int shape, value;
};

card cards[8];
bool status[9];
int nums[14];
int shapes[4];
int answer = 0;

void check(vector<int>& visited) {
    memset(status, false, sizeof(status));
    memset(nums, 0, sizeof(nums));
    memset(shapes, 0, sizeof(shapes));
    status[0] = true;

    for (auto idx : visited) {
        int s, v;
        s = cards[idx].shape;
        v = cards[idx].value;

        shapes[s]++;
        nums[v]++;

        if (shapes[s] == 5) status[5] = true;
    }

    int pair = 0;
    for (int i = 1; i < 14; i++) {
        if (nums[i] == 2) {
            status[1] = true;
            pair++;
        }
        if (nums[i] == 3) status[3] = true;
        if (nums[i] == 4) status[7] = true;
    }

    if (pair >= 2) status[2] = true;
    if (pair >= 1 && status[3]) status[6] = true;

    // Straight check
    bool flag = false;
    for (int i = 1; i <= 10; i++) {
        int cnt = 0;
        for (int j = 0; j < 5; j++) {
            int idx = i + j;
            if (idx > 13) idx -= 13;
            if (nums[idx] != 1) {
                break;
            }
            cnt++;
        }

        if (cnt == 5) {
            status[4] = true;
            break;
        }
    }

    if (status[4] && status[5]) status[8] = true;

    for (int i = 8; i >= 0; i--) {
        if (answer < i) {
            if (status[i]) {
                answer = i;
                break;
            }
        } else {
            break;
        }
    }
}

void comb(int cur, vector<int>& visited) {
    if (visited.size() == 5) {
        check(visited);
        return;
    }

    for (int i = cur + 1; i <= 7; i++) {
        if (cur == 0 && i > 3) break;
        visited.push_back(i);
        comb(i, visited);
        visited.pop_back();
    }
}

int main(int argc, char** argv) {
    int T;

    cin >> T;

    memset(cards, 0, sizeof(cards));
    for (int test_case = 1; test_case <= T; ++test_case) {
        // card init
        for (int i = 1; i <= 7; i++) {
            int n;
            char m;
            cin >> m >> n;

            // C D H S
            int s;
            if (m == 'C') {
                s = 0;
            } else if (m == 'D') {
                s = 1;
            } else if (m == 'H') {
                s = 2;
            } else {
                s = 3;
            }

            cards[i].shape = s;
            cards[i].value = (n == 14) ? 1 : n;
        }

        answer = 0;

        vector<int> visited;
        comb(0, visited);

        cout << "#" << test_case << " " << jokbos[answer] << endl;
    }

    return 0;
}