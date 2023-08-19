#include <iostream>
#include <vector>

using namespace std;

int finalValueAfterOperations(vector<string>& operations) {
    int x = 0;
    for (auto op : operations) {
        if (op == "--X") {
            --x;
        } else if (op == "X--") {
            x--;
        } else if (op == "++X") {
            ++x;
        } else {
            x++;
        }
    }

    return x;
}

int main() {
    vector<string> operations = {"--X", "X++", "X++"};
    int result = finalValueAfterOperations(operations);

    cout << result << endl;
}