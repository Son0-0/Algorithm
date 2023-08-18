#include <cmath>
#include <iostream>

using namespace std;

int calculate(string target) {
    int result = 0;
    int targetLength = target.size() - 1;

    for (auto c : target) {
        result += (c - 'a') * pow(10, targetLength--);
    }

    return result;
}

bool isSumEqual(string firstWord, string secondWord, string targetWord) {
    int first, second, target;

    first = calculate(firstWord);
    second = calculate(secondWord);
    target = calculate(targetWord);

    return (first + second) == target;
}

int main() {
    bool result = isSumEqual("acb", "cba", "cdb");
    cout << result << endl;
}