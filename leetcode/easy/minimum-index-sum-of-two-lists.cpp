#include <iostream>
#include <vector>

using namespace std;

vector<string> findRestaurant(vector<string> &list1, vector<string> &list2)
{
    vector<int> temp(list1.size(), -1);
    int min = 2001;

    for (int i = 0; i < list2.size(); i++)
    {
        for (int j = 0; j < list1.size(); j++)
        {
            if (list2[i] == list1[j])
            {
                temp[j] = j + i;

                if (temp[j] < min)
                {
                    min = temp[j];
                }
            }
        }
    }

    vector<string> result;

    for (int i = 0; i < list1.size(); i++)
    {
        if (temp[i] == min)
        {
            result.push_back(list1[i]);
        }
    }

    return result;
}

int main()
{
    vector<string> list1{"Shogun", "Tapioca Express", "Burger King", "KFC"};
    vector<string> list2{"KFC", "Shogun", "Burger King"};

    vector<string> result = findRestaurant(list1, list2);
    for (const auto &item : result)
    {
        cout << item << " ";
    }
}