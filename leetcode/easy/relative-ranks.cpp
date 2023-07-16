#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

vector<string> findRelativeRanks(vector<int> &score)
{
    vector<string> result(score.size(), "");

    priority_queue<vector<int>> pq;

    for (int i = 0; i < score.size(); i++)
    {
        pq.push(vector<int>{score[i], i});
    }

    for (int i = 1; i <= score.size(); i++)
    {
        vector<int> target = pq.top();
        pq.pop();

        switch (i)
        {
        case 1:
            result[target[1]] = "Gold Medal";
            break;
        case 2:
            result[target[1]] = "Silver Medal";
            break;
        case 3:
            result[target[1]] = "Bronze Medal";
            break;
        default:
            result[target[1]] = to_string(i);
            break;
        }
    }

    return result;
}

int main(void)
{
    vector<int> nums{5, 4, 3, 2, 1};

    vector<string> result = findRelativeRanks(nums);

    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << endl;
    }
}