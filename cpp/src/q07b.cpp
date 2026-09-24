#include <iostream>
#include <queue>
#include <vector>
#include <utility>

using Item = std::pair<int,int>;    // 要素の型に別名を付ける（問3）。以下が読みやすくなる

// .first が小さい要素を先に取り出すための比較ファンクタ
class paircomp {
public:
    bool operator()(const Item& a, const Item& b) const {
        return a.first > b.first;   // 「a を b より後ろにする」条件
    }
};

int main() {
    // priority_queue のテンプレート引数は3つ：
    //   <要素の型, 内部で要素を保管する入れ物の型, 比較のしかた>
    // 3つ目（比較）を変えたいので、途中の2つ目（入れ物）も省略せずに書く
    std::priority_queue<Item,               // 要素の型
                        std::vector<Item>,  // 入れ物（ほぼ常に vector<要素の型>）
                        paircomp> pq;       // 比較ファンクタ
    // {3, 300} は std::pair<int,int>{3, 300} の短い書き方（波カッコで pair を作る）
    pq.push({3, 300});          // std::make_pair(3, 300) と書いても同じ
    pq.push({1, 100});
    pq.push({2, 200});

    while (!pq.empty()) {
        auto p = pq.top();          // first が一番小さいものが出てくる
        pq.pop();
        std::cout << p.first << " => " << p.second << "\n";
    }
    // 出力: 1 => 100 / 2 => 200 / 3 => 300（first の昇順）
    return 0;
}
