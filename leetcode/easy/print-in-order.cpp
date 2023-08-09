#include <atomic>
#include <functional>
#include <iostream>
#include <thread>
#include <vector>

using namespace std;

class Foo {
   public:
    Foo() { atomic_init(&AtomicCount, 1); }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        while (AtomicCount != 1) {
            cout << "busy waiting";
            this_thread::yield();
        }
        printFirst();
        AtomicCount++;
    }

    void second(function<void()> printSecond) {
        // printSecond() outputs "second". Do not change or remove this line.
        while (AtomicCount != 2) {
            this_thread::yield();
        }
        printSecond();
        AtomicCount++;
    }

    void third(function<void()> printThird) {
        // printThird() outputs "third". Do not change or remove this line.
        while (AtomicCount != 3) {
            this_thread::yield();
        }
        printThird();
        AtomicCount++;
    }

   private:
    atomic<int> AtomicCount;
};

int main() {
    Foo foo;
    vector<int> nums = {1, 2, 3};
    vector<thread> threads;

    auto printFirst = []() { cout << "first"; };
    auto printSecond = []() { cout << "second"; };
    auto printThird = []() { cout << "third"; };

    for (int num : nums) {
        if (num == 1)
            threads.emplace_back(&Foo::first, &foo, printFirst);
        else if (num == 2)
            threads.emplace_back(&Foo::second, &foo, printSecond);
        else if (num == 3)
            threads.emplace_back(&Foo::third, &foo, printThird);
    }

    for (auto &t : threads) {
        t.join();
    }

    return 0;
}