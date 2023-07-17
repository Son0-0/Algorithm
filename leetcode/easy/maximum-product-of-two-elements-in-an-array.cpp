#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int maxProduct(vector<int> &nums)
{
    priority_queue<int> pq;

    for (auto num : nums)
    {
        pq.push(num);
    }

    int a = pq.top() - 1;
    pq.pop();
    int b = pq.top() - 1;

    return a * b;
}

int main()
{
    vector<int> nums{3, 4, 5, 2};

    int result = maxProduct(nums);

    cout << result << "\n";
}