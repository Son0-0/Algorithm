#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

int maximumScore(int a, int b, int c) {
    priority_queue<int> pq;

    pq.push(a);
    pq.push(b);
    pq.push(c);

    int result = 0;
    while (pq.size() >= 2) {
        int first = pq.top();
        pq.pop();

        int second = pq.top();
        pq.pop();

        if (first != 1) {
            pq.push(first - 1);
        }

        if (second != 1) {
            pq.push(second - 1);
        }

        result++;
    }

    return result;
}

int main() {
    int result = maximumScore(2, 4, 6);
    cout << result << "\n";

    result = maximumScore(4, 4, 6);
    cout << result << "\n";

    result = maximumScore(1, 8, 8);
    cout << result << "\n";
}