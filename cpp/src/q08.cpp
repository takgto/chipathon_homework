#include <iostream>
#include <memory>

struct Buf {                         // 確保・解放が見えるように表示するだけの型
    Buf()  { std::cout << "  確保\n"; }
    ~Buf() { std::cout << "  解放\n"; }
};

void rawPointer() {
    std::cout << "[生のポインタ]\n";
    Buf* p = new Buf;
    // ... ここで return や例外があると delete に届かず「解放」が出ない（メモリリーク）
    delete p;                        // 自分で書かないと解放されない
}

void smartPointer() {
    std::cout << "[unique_ptr]\n";
    auto p = std::make_unique<Buf>();
    // delete を書かない。関数を抜けるとき（スコープの終わり）に自動で解放される
}

int main() {
    rawPointer();
    smartPointer();

    // 配列は new[] ↔ delete[] が対
    int8_t* arr = new int8_t[1024];
    arr[0] = 1;
    delete[] arr;                    // delete arr; は誤り

    std::cout << "done\n";
    return 0;
}
