#include <iostream>
#include <thread>
#include <queue>
#include <mutex>
#include <string>

// キューから1つ取り出して処理する。空になったら終了
void worker(int id, std::queue<int>& q, std::mutex& m) {
    while (true) {
        int item;
        {
            std::lock_guard<std::mutex> lock(m); // 触るのは一度に1スレッドだけ
            if (q.empty()) return;
            item = q.front();
            q.pop();
        }
        // 1行分をまとめて出す（複数スレッドが同時に表示すると行が混ざることがあるため）
        std::string line = "thread " + std::to_string(id) + " が " + std::to_string(item) + " を処理\n";
        std::cout << line;
    }
}

int main() {
    std::queue<int> q;                    // 共有するキュー（1個だけ）
    std::mutex m;
    for (int i = 1; i <= 6; i++) q.push(i);

    std::thread t1(worker, 1, std::ref(q), std::ref(m)); // std::ref で「同じ q」を渡す
    std::thread t2(worker, 2, std::ref(q), std::ref(m));
    t1.join();
    t2.join();
    std::cout << "元の q に残っている個数 = " << q.size() << "\n";   // 0（2人で6個を分担した）
    return 0;
}
