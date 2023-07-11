#include <iostream>
#include <vector>

using namespace std;

int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
    int count = 0;
    int size = arr.size();

    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
        for (int k = j + 1; k < size; k++) {
            if (abs(arr[i] - arr[j]) <= a && abs(arr[j] - arr[k]) <= b &&
                abs(arr[i] - arr[k]) <= c) {
            count++;
            }
        }
        }
    }
    return count;
}

int main() {
  vector<int> nums{3, 0, 1, 1, 9, 7};
  int result = countGoodTriplets(nums, 7, 2, 3);

  cout << result;
}