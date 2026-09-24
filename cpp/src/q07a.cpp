#include <iostream>
#include <string>

// 1. ファンクタ（() で呼べるクラス）
class Mul {
public:
    int operator()(int a, int b) { return a * b; }
};

// 2. テンプレートクラス
template<typename T>
class Box {
    T value_;
public:
    Box(T v) : value_(v) {}
    T get() { return value_; }
};

int main() {
    Mul m;
    std::cout << m(3, 4) << "\n";      // 12  ← m(...) が呼び出せる

    Box<int> bi(5);
    Box<std::string> bs("hi");
    std::cout << bi.get() << " " << bs.get() << "\n"; // 5 hi
    return 0;
}
