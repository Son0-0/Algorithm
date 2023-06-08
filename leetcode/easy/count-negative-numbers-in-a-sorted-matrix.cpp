#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countNegatives(vector<vector<int>>& grid) {
	int result = 0;
	int row = grid.size()-1;
	int col = grid[0].size()-1;

	for (int i = 0; i <= row; i++) {
		for (int j = col; j >= 0; j--) {
			if (grid[i][j] < 0) {
				result++;
			}
			else {
				break;
			}
		}
	}

	return result;
}


int main(void) {
	vector<vector<int>> arr{{4, 3, 2, -1}, { 3,2,1,-1 }, { 1,1,-1,-2 }, { -1,-1,-2,-3 }};

	cout << countNegatives(arr) << endl;
}