#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<int> kWeakestRows(vector<vector<int>> &mat, int k)
{
    priority_queue<pair<int, int>, vector<pair<int, int>>,
                   greater<pair<int, int>>>
        pq;

    for (int i = 0; i < mat.size(); i++)
    {
        int cnt = 0;
        for (int j = 0; j < mat[0].size(); j++)
        {
            if (mat[i][j] == 1)
            {
                cnt++;
            }
        }
        pq.push({cnt, i});
    }

    vector<int> result;

    for (int i = 0; i < k; i++)
    {
        result.push_back(pq.top().second);
        pq.pop();
    }

    return result;
}

int main()
{
    vector<vector<int>> matrix = {
        {1, 0, 0, 0}, {1, 1, 1, 1}, {1, 0, 0, 0}, {1, 0, 0, 0}};

    vector<int> result = kWeakestRows(matrix, 2);

    for (auto num : result)
    {
        cout << num << " ";
    }
}