#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

int secondHighest(string s) {
    set<int> nums;
    for (auto c : s) {
        if ('0' <= c && c <= '9') {
            nums.insert(c - '0');
        }
    }

    if (nums.size() < 2) {
        return -1;
    }

    auto first = nums.rbegin();

    return *(++first);
}

int main() {
    int result = secondHighest("dfa12321afd");
    cout << result << endl;
}