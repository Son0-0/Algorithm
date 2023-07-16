#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(int a, int b)
{
    return a > b;
}

bool canMakeArithmeticProgression(vector<int> &arr)
{
    sort(arr.begin(), arr.end());

    int diff = arr[1] - arr[0];
    int temp = 0;

    for (int i = 2; i < arr.size(); i++)
    {
        temp = arr[i] - arr[i - 1];

        if (diff != temp)
        {
            return false;
        }
    }

    return true;
}

int main(void)
{
    vector<int> arr{3, 5, 1};

    cout << canMakeArithmeticProgression(arr) << endl;

    arr = {1, 2, 4};

    cout << canMakeArithmeticProgression(arr) << endl;
}