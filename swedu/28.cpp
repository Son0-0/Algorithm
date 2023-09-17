#include <iostream>
#include <vector>

using namespace std;

vector<int> arr;
vector<int> tmp;
long long ans;

void mergeSort(int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        mergeSort(start, mid);
        mergeSort(mid + 1, end);

        int left = start, right = mid + 1;
        int idx = start;

        while (left <= mid || right <= end) {
            if (right > end || (left <= mid && arr[left] < arr[right])) {
                tmp[idx++] = arr[left++];
            } else {
                ans += (mid - left + 1);
                tmp[idx++] = arr[right++];
            }
        }
        for (int i = start; i <= end; i++) arr[i] = tmp[i];
    }
}

int main() {
    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        ans = 0;
        int n;
        cin >> n;

        arr.resize(n);
        tmp.resize(n);

        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        mergeSort(0, n - 1);

        cout << "#" << test_case << " " << ans << endl;
    }
    return 0;
}