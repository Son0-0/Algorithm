#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

char nextGreatestLetter(vector<char>& letters, char target) {
    for (int i = 0; i < letters.size(); i++) {
        if (target < letters[i]) {
            return letters[i];
        }
    }

    return letters[0];
}


int main(void) {
	vector<char> arr{'c', 'f', 'j'};

	cout << nextGreatestLetter(arr, 'a') << endl;
}