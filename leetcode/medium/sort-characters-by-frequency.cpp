#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

string frequencySort(string s)
{
    map<char, int> m;
    priority_queue<pair<int, char>> pq;

    for (int i = 0; i < s.size(); i++)
    {
        m[s[i]]++;
    }

    for (const auto &item : m)
    {
        pq.push({item.second, item.first});
    }

    string result = "";

    while (!pq.empty())
    {
        for (int i = 0; i < pq.top().first; i++)
        {
            result += pq.top().second;
        }
        pq.pop();
    }

    return result;
}

int main()
{
    string result = frequencySort("tree");

    cout << result << "\n";
}

// user's solution
// class Solution
// {
// public:
//     string frequencySort(string s)
//     {
//         priority_queue<pair<int, char>> pq;
//         unordered_map<char, int> m;

//         for (auto &i : s)
//         {
//             m[i]++;
//         }

//         for (auto it : m)
//         {
//             pq.push({it.second, it.first});
//         }

//         string ans = "";

//         while (!pq.empty())
//         {
//             int x = pq.top().first;
//             while (x--)
//             {
//                 ans += pq.top().second;
//             }

//             pq.pop();
//         }

//         return ans;
//     }
// };