#include <iostream>
int main(int argc, char** argv) {
    if (argc != 3) {                       // プログラム名+引数2個=3 でなければ
        std::cout << "Usage: " << argv[0] << " <model> <video>\n";
        return -1;                         // 引数が足りないので終了
    }
    std::cout << "argc = " << argc << "\n";
    for (int i = 0; i < argc; i++)
        std::cout << "argv[" << i << "] = " << argv[i] << "\n";
    return 0;
}
