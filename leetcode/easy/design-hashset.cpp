#include <iostream>
#include <unordered_map>

using namespace std;

class MyHashSet {
    unordered_map<int, bool> um;

   public:
    MyHashSet() {}

    void add(int key) { um[key] = true; }

    void remove(int key) {
        if (um.find(key) != um.end()) {
            um.erase(key);
        }
    }

    bool contains(int key) {
        if (um.find(key) != um.end()) {
            return true;
        }
        return false;
    }
};

int main() {
    MyHashSet* obj = new MyHashSet();
    obj->add(3);
    obj->remove(3);
    bool result = obj->contains(3);
    cout << result << endl;
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */