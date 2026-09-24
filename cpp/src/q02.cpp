#include <iostream>
#include <vector>
int main() {
    std::vector<int> v;          // 1. 空のvector
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    std::cout << "size = " << v.size() << "\n";   // 3

    for (auto x : v)             // 2. 範囲for
        std::cout << x << " ";
    std::cout << "\n";

    std::vector<float> result(5);  // 3. 要素5個（初期値0.0）で作る
    std::cout << "result size = " << result.size() << "\n";
    return 0;
}
