#include <iostream>
#include <chrono>
using namespace std::chrono;

long g_callCount = 0;                // グローバル変数：add が呼ばれた回数を記録

int add(int a, int b) {
    g_callCount++;                   // どの関数からでも触れる（グローバル）
    return a + b;
}

int main() {
    const int N = 100000000;         // ローカル変数（main の中だけ有効）
    long sum = 0;                    // ローカル変数

    auto t0 = system_clock::now();
    for (int i = 0; i < N; i++)
        sum = add(sum % 1000, i % 1000);   // add を N 回呼ぶ
    auto t1 = system_clock::now();

    std::cout << "sum = " << sum << "\n";
    std::cout << "add を呼んだ回数(global) = " << g_callCount << "\n";
    std::cout << "所要時間 = "
              << duration_cast<milliseconds>(t1 - t0).count() << " ms\n";
    return 0;
}
