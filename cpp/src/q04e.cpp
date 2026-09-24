#include <iostream>
#include <vector>

// 参照で受け取る：呼び出し側の v をそのまま指す。「無い」ことはあり得ない
int sumRef(const std::vector<int>& v) {
    int s = 0;
    for (int x : v) s += x;       // 値と同じ書き方で中身に触れる
    return s;
}

// ポインタで受け取る：アドレスを受け取る。nullptr（何も指していない）があり得る
int sumPtr(const std::vector<int>* p) {
    if (p == nullptr) return 0;   // ← 参照には無い「無い場合」の分岐
    int s = 0;
    for (int x : *p) s += x;      // 中身に触るには *p か p->
    return s;
}

int main() {
    std::vector<int> a = {1, 2, 3};
    std::vector<int> b = {10, 20, 30};

    // --- 呼び出し側の見た目 ---
    std::cout << "sumRef(a)  = " << sumRef(a)  << "\n";   // 値渡しと同じ見た目
    std::cout << "sumPtr(&a) = " << sumPtr(&a) << "\n";   // & でアドレスを渡す

    // --- ポインタだけができること① 「無い」を渡す ---
    std::cout << "sumPtr(nullptr) = " << sumPtr(nullptr) << "\n";
    // sumRef(nullptr) はコンパイルエラー。参照は必ず実体を指す

    // --- ポインタだけができること② 指す先を途中で変える ---
    const std::vector<int>* p = &a;
    std::cout << "p -> a : " << sumPtr(p) << "\n";
    p = &b;                                              // 指す先を b に付け替える
    std::cout << "p -> b : " << sumPtr(p) << "\n";

    const std::vector<int>& r = a;                       // 参照は最初に指した a から変えられない
    std::cout << "r -> a : " << sumRef(r) << "\n";
    // r = b; と書いても「r が b を指す」のではなく「a に b の中身をコピーする」意味になる（const なのでエラー）

    // --- ポインタだけができること③ 配列の先頭アドレス＋個数で扱う ---
    int buf[4] = {5, 6, 7, 8};
    int* q = buf;                                        // 配列名は先頭要素のアドレス
    std::cout << "q[0]=" << q[0] << "  *(q+2)=" << *(q + 2) << "\n";   // アドレス計算ができる
    return 0;
}
