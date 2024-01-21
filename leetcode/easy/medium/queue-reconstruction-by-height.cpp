#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool comp(const vector<int>& a, const vector<int>& b) {
    if (a[0] == b[0]) return a[1] < b[1];
    return a[0] > b[0];
}

vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
    sort(people.begin(), people.end(), comp);

    vector<vector<int>> ans;
    for (auto person : people) {
        ans.insert(ans.begin() + person[1], person);
    }

    return ans;
}

int main() {
    vector<vector<int>> people = {{7, 0}, {4, 4}, {7, 1},
                                  {5, 0}, {6, 1}, {5, 2}};
    vector<vector<int>> result = reconstructQueue(people);

    for (auto r : result) {
        cout << r[0] << " " << r[1] << endl;
    }
}

// class Solution {
// public:
//     static bool comp(const vector<int> &a, const vector<int> &b) {
//         if (a[0] == b[0])
//             return a[1] < b[1];
//         return a[0] > b[0];
//     }

//     vector<vector<int>> reconstructQueue(vector<vector<int>> &people) {
//         sort(people.begin(), people.end(), comp);

//         vector<vector<int>> ans;
//         for (auto person : people) {
//             ans.insert(ans.begin() + person[1], person);
//         }

//         return ans;
//     }
// };