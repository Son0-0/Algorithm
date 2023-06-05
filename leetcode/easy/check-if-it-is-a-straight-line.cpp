#include <iostream>
#include <vector>

using namespace std;

bool checkStraightLine(vector<vector<int>>& coordinates) {
    int x, y;

    x = coordinates[0][0] - coordinates[1][0];
    y = coordinates[0][1] - coordinates[1][1];

    
    for (int i = 2; i < coordinates.size(); i++) {
        if (y * (coordinates[i][0] - coordinates[0][0]) != x * (coordinates[i][1] - coordinates[0][1])) {
            return false;
        }
    }

    return true;
}

int main(void) {
	vector<vector<int>> cd{{1, 2}, { 2, 3 }, { 3, 4 }, { 4, 5 }, { 5, 6 }, { 6, 7 }};

	cout << checkStraightLine(cd) << endl;

	cd = { {1, 1}, {2, 2}, {3, 4}, {4, 5}, {5, 6}, {7, 7} };
	
	cout << checkStraightLine(cd) << endl;

    cd = { {1, 2}, {1, 3}, {1, 4}, {1, 5}, {1, 6}, {6, 7} };

    cout << checkStraightLine(cd) << endl;
}