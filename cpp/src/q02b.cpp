#include <iostream>
#include <vector>
// push_back で増やしていくと、容量(capacity)が足りなくなるたびに「再確保＋全要素コピー」が起きる。
// capacity() の変化を観察する。
int main() {
    std::vector<int> v;
    std::size_t last = 0;
    for (int i = 0; i < 1000; i++) {
        v.push_back(i);
        if (v.capacity() != last) {             // 容量が変わった＝再確保が起きた
            last = v.capacity();
            std::cout << "size=" << v.size() << "  capacity=" << v.capacity() << "\n";
        }
    }

    std::vector<int> w(1000);                   // 最初から 1000 個で確保
    std::cout << "\nw: size=" << w.size() << "  capacity=" << w.capacity()
              << "  (再確保なし)\n";
    return 0;
}
