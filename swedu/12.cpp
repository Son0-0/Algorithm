#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

vector<vector<pair<int, int>>> tree;
map<int, set<int>> parents;
map<int, map<int, int>> order;

int tree_size;

void find_parent(int n, int idx, int count = 0) {
    for (auto i : tree[idx]) {
        if (i.second) {
            parents[n].insert(i.first);
            order[n][i.first] = count;
            find_parent(n, i.first, count + 1);
        }
    }
}

void find_tree(int n) {
    for (auto i : tree[n]) {
        if (!i.second) {
            tree_size++;
            find_tree(i.first);
        }
    }
}

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        tree_size = 1;
        int V, E, A, B;
        cin >> V >> E >> A >> B;
        vector<int> temp(2 * E);

        for (int i = 0; i < 2 * E; i++) {
            cin >> temp[i];
        }

        tree.resize(V + 1);
        for (int i = 0; i < 2 * E; i += 2) {
            int a = temp[i];
            int b = temp[i + 1];
            tree[a].push_back(make_pair(b, 0));
            tree[b].push_back(make_pair(a, 1));
        }

        find_parent(A, A);
        find_parent(B, B);

        set<int> candidatekey;
        for (int i : parents[A]) {
            if (parents[B].count(i)) {
                candidatekey.insert(i);
            }
        }

        int distance = 999;
        int my_parent = -1;

        for (int i : candidatekey) {
            if (order[A][i] < distance) {
                distance = order[A][i];
                my_parent = i;
            }
        }

        find_tree(my_parent);

        cout << "#" << t + 1 << " " << my_parent << " " << tree_size << endl;

        tree.clear();
        parents.clear();
        order.clear();
    }

    return 0;
}