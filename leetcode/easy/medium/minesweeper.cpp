#include <iostream>
#include <queue>
#include <set>
#include <vector>

using namespace std;

vector<int> dx = {-1, -1, -1, 0, 1, 1, 1, 0};
vector<int> dy = {-1, 0, 1, 1, 1, 0, -1, -1};

int getNumberOfMine(vector<vector<char>> &board, int x, int y, int m, int n) {
    int count = 0;
    int nx, ny;

    for (int i = 0; i < 8; i++) {
        nx = x + dx[i];
        ny = y + dy[i];

        if ((0 <= nx && nx < m) && (0 <= ny && ny < n)) {
            if (board[nx][ny] == 'M') {
                count++;
            }
        }
    }

    return count;
}

vector<vector<char>> updateBoard(vector<vector<char>> &board,
                                 vector<int> &click) {
    queue<pair<int, int>> q;

    int m = board.size();
    int n = board[0].size();

    int cx = click[0];
    int cy = click[1];

    if (board[cx][cy] == 'M') {
        board[cx][cy] = 'X';
        return board;
    }

    q.push(make_pair(cx, cy));

    while (!q.empty()) {
        auto cur = q.front();
        q.pop();

        cx = cur.first;
        cy = cur.second;

        int count = getNumberOfMine(board, cx, cy, m, n);

        if (count > 0) {
            board[cx][cy] = char(count + '0');
        } else {
            board[cx][cy] = 'B';

            for (int i = 0; i < 8; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if ((0 <= nx && nx < m) && (0 <= ny && ny < n)) {
                    if (board[nx][ny] == 'E') {
                        q.push(make_pair(nx, ny));
                        board[nx][ny] = 'B';
                    }
                }
            }
        }
    }

    return board;
}

int main() {
    vector<vector<char>> board = {{'E', 'E', 'E', 'E', 'E'},
                                  {'E', 'E', 'M', 'E', 'E'},
                                  {'E', 'E', 'E', 'E', 'E'},
                                  {'E', 'E', 'E', 'E', 'E'}};
    vector<int> click = {3, 0};

    // vector<vector<char>> board = {{'B', '1', 'E', '1', 'B'},
    //                               {'B', '1', 'M', '1', 'B'},
    //                               {'B', '1', '1', '1', 'B'},
    //                               {'B', 'B', 'B', 'B', 'B'}};
    // vector<int> click = {1, 2};
    vector<vector<char>> result = updateBoard(board, click);

    for (auto row : result) {
        for (auto elem : row) {
            cout << elem << " ";
        }
        cout << endl;
    }
}