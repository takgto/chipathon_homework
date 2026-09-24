#include <iostream>
#include <vector>

// 値渡し：v のコピーが作られる（大きいと遅い）。元は変わらない
void byValue(std::vector<int> v) {
    v[0] = 999;                 // コピーを書き換えるだけ。呼び出し側は変わらない
}

// const参照：コピーしない（速い）。中身は読むだけで書き換え不可
int sumByRef(const std::vector<int>& v) {
    int s = 0;
    for (int x : v) s += x;     // v[0] = 999; と書くとコンパイルエラー（const）
    return s;
}

// 非const参照：コピーせず、元のデータを直接書き換えられる
void doubleByRef(std::vector<int>& v) {
    for (int& x : v) x *= 2;    // 呼び出し側の v がそのまま変わる
}

int main() {
    std::vector<int> data = {1, 2, 3};

    byValue(data);
    std::cout << "byValue後 data[0] = " << data[0] << "\n";      // 1 のまま

    std::cout << "合計 = " << sumByRef(data) << "\n";            // 6（読むだけ）

    doubleByRef(data);
    std::cout << "doubleByRef後 data[0] = " << data[0] << "\n";  // 2（書き換わる）
    return 0;
}
