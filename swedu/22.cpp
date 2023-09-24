#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

int flipCount;
vector<pair<int, int>> flipResults;
vector<int> subSumArray;

string reverseOperation(int left, int right, string str) {
    int start = left, end = right;
    while (left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }

    for (int i = start; i <= end; i++) {
        if (str[i] == '(')
            str[i] = ')';
        else if (str[i] == ')')
            str[i] = '(';
    }

    return str;
}

string flipParentheses(string str, int length) {
    int minValue = 0, position = -1, sum = 0;
    for (int i = 0; i < length; i++) {
        if (str[i] == '(')
            sum++;
        else if (str[i] == ')')
            sum--;

        if (sum < minValue) {
            minValue = sum;
            position = i;
        }
    }

    if (position != -1) {
        flipCount++;
        flipResults.push_back(make_pair(0, position));
        str = reverseOperation(0, position, str);
    }

    return str;
}

void solveParentheses(string str, int length) {
    if (length % 2 == 1) {
        flipCount = -1;
        return;
    }

    str = flipParentheses(str, length);

    int sum = 0;
    for (int i = 0; i < length; i++) {
        if (str[i] == '(')
            sum++;
        else if (str[i] == ')')
            sum--;
        subSumArray.push_back(sum);
    }

    if (subSumArray.back() == 0) return;

    int halfSum = subSumArray.back() / 2;
    int position = -1;
    for (int i = 0; i < length; i++) {
        if (halfSum == subSumArray.at(i)) {
            position = i + 1;
        }
    }
    flipResults.push_back(make_pair(position, length - 1));
    flipCount++;
}

int main(void) {
    int testCases;
    cin >> testCases;
    for (int tc = 1; tc <= testCases; tc++) {
        int length;
        string inputString;
        cin >> length >> inputString;

        flipCount = 0;
        subSumArray.clear();
        flipResults.clear();

        solveParentheses(inputString, length);

        printf("#%d %d\n", tc, flipCount);
        for (int i = 0; i < flipResults.size(); i++) {
            printf("%d %d\n", flipResults[i].first, flipResults[i].second);
        }
    }
    return 0;
}
