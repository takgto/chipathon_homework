#include <iostream>
#include <vector>
#include <chrono>
using namespace std::chrono;

// 「画像1枚」のつもりの大きなデータ（int 300万個 ≒ 12MB）
long byValue(std::vector<int> v)        { return v[0]; }   // 毎回コピーされる
long byRef(const std::vector<int>& v)   { return v[0]; }   // コピーされない

int main() {
    std::vector<int> img(3000000, 1);
    const int N = 100;                   // 100 回呼ぶ
    long s = 0;

    auto t0 = system_clock::now();
    for (int i = 0; i < N; i++) s += byValue(img);
    auto t1 = system_clock::now();
    for (int i = 0; i < N; i++) s += byRef(img);
    auto t2 = system_clock::now();

    std::cout << "値渡し   " << N << "回: " << duration_cast<milliseconds>(t1 - t0).count() << " ms\n";
    std::cout << "参照渡し " << N << "回: " << duration_cast<milliseconds>(t2 - t1).count() << " ms\n";
    return s == 0;   // s を使って最適化で消されないようにしているだけ
}
