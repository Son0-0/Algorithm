#include <iostream>

using namespace std;

int arr[5] = {1, 2, 3, 4, 5};
int segtree[5 << 2];
int lazy[5 << 2];
int N = 5;

void push(int node, int left, int right) {
    if (lazy[node]) {
        segtree[node] += (right - left + 1) * lazy[node];
        if (left < right) {
            lazy[node << 1] += lazy[node];
            lazy[(node << 1) + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update(int start, int end, int value) {
    start += N;
    end += N;

    while (start <= end) {
        if (start % 2 == 1) {
            lazy[start] += value;
            push(start, start >> 1, (start - 1) >> 1);
            start++;
        }

        if (end % 2 == 0) {
            lazy[end] += value;
            push(end, (end + 1) >> 1, end >> 1);
            end--;
        }

        start >>= 1;
        end >>= 1;
    }
}

int query(int left, int right) {
    left += N;
    right += N;

    int sum = 0;
    while (left < right) {
        if (left & 1) {
            push(left, left >> 1, right >> 1);
            sum += segtree[left];
            left++;
        }

        if (right & 1) {
            right--;
            push(right, left >> 1, right >> 1);
            sum += segtree[right];
        }

        left >>= 1;
        right >>= 1;
    }

    return sum;
}

int main() {
    for (int i = 0; i < N; i++) segtree[i + N] = arr[i];

    for (int i = N; i > 0; i--)
        segtree[i] = segtree[i << 1] + segtree[(i << 1) + 1];

    // 1 2 3 4 5
    update(3 - 1, 4 - 1, 6);
    // 1 2 9 10 5
    cout << query(2 - 1, 5 - 1) << endl;
    // 26
    update(1 - 1, 3 - 1, -2);
    // -1 1 6 10 5
    cout << query(2 - 1, 5 - 1) << endl;
    // 22
}