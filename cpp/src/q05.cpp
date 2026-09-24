#include <iostream>
#include <chrono>
using namespace std::chrono;

int main() {
    auto t0 = system_clock::now();
    // ここに時間を測りたい処理を書く（例：大きめのループ）
    long sum = 0;
    for (long i = 0; i < 100000000L; i++) sum += i;
    auto t1 = system_clock::now();

    std::cout << duration_cast<milliseconds>(t1 - t0).count() << " ms\n";
    return 0;
}
