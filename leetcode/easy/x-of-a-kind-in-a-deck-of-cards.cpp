#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>

using namespace std;

bool hasGroupsSizeX(vector<int>& deck) {
    int n = deck.size();

    if (n % 2 == 1) {
        return false;
    }

    unordered_map<int, int> um;

    for (auto num : deck) {
        um[num]++;
    }

    int gcd = um.begin()->second;
    for (auto elem : um) {
        gcd = __gcd(gcd, elem.second);
    }

    return gcd != 1;
}

int main() {
    vector<int> deck = {1, 2, 3, 4, 4, 3, 2, 1};
    cout << hasGroupsSizeX(deck) << endl;
}