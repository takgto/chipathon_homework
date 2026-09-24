#include <iostream>
#include <vector>
int main() {
    std::vector<float> v(5);          // 要素5個。規格で「0 で初期化される」と決まっている
    float* p = new float[5];          // 要素5個。初期化されない（何が入っているかは不定）

    std::cout << "vector<float> v(5) : ";
    for (int i = 0; i < 5; i++) std::cout << v[i] << " ";
    std::cout << "\nnew float[5]       : ";
    for (int i = 0; i < 5; i++) std::cout << p[i] << " ";   // 0 に見えることもあるが、保証はない
    std::cout << "\n";

    delete[] p;
    return 0;
}
