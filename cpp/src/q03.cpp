#include <iostream>
#include <utility>
#include <string>

using imagePair = std::pair<int, std::string>;  // 3. 型に別名を付ける

int main() {
    std::pair<int, std::string> p(1, "cat");     // 1.
    std::cout << p.first << " " << p.second << "\n";

    auto q = std::make_pair(2, std::string("dog")); // 2. auto で受ける
    std::cout << q.first << " " << q.second << "\n";

    imagePair r = std::make_pair(3, std::string("bird")); // 別名を使う
    std::cout << r.first << " " << r.second << "\n";
    return 0;
}
