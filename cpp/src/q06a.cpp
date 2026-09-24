#include <iostream>

int add(int a, int b) {              // 関数定義（値渡し）
    return a + b;
}

int main() {
    std::cout << add(3, 4) << "\n";  // 7
    return 0;
}
