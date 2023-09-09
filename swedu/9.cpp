#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

vector<string> nums = {"ZRO", "ONE", "TWO", "THR", "FOR",
                       "FIV", "SIX", "SVN", "EGT", "NIN"};

int convertToInt(string target) {
    for (int i = 0; i < 10; i++) {
        if (target == nums[i]) return i;
    }
}

int main() {
    int test_case;
    int T;

    scanf("%d\n", &T);

    for (test_case = 1; test_case <= T; test_case++) {
        int tc, length;
        scanf("%d %d\n", &tc, &length);

        char word[100001];
        length = 3 * length + length;

        fgets(word, length, stdin);

        word[length - 1] = ' ';
        word[length++] = '\0';

        string num = "";
        int convertedNum = 0;
        priority_queue<int, vector<int>, greater<int>> pq;

        int i = 0;
        for (i = 0; i < length; i++) {
            if (word[i] == ' ') {
                convertedNum = convertToInt(num);
                pq.push(convertedNum);
                num = "";
            } else {
                num += word[i];
            }
        }

        int size = pq.size();
        printf("#%d\n", test_case);

        while (!pq.empty()) {
            cout << nums[pq.top()] << " ";
            pq.pop();
        }

        cout << endl;
    }
}