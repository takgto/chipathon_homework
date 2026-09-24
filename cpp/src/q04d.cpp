#include <iostream>
#include <thread>
#include <queue>
#include <mutex>
#include <string>

// ans4c.cpp と同じ worker。ただし q を「コピー」で受け取る（& を外した）
void worker(int id, std::queue<int> q, std::mutex& m) {
    while (true) {
        int item;
        {
            std::lock_guard<std::mutex> lock(m);
            if (q.empty()) return;
            item = q.front();
            q.pop();
        }
        std::string line = "thread " + std::to_string(id) + " が " + std::to_string(item) + " を処理\n";
        std::cout << line;
    }
}

int main() {
    std::queue<int> q;
    std::mutex m;
    for (int i = 1; i <= 6; i++) q.push(i);

    std::thread t1(worker, 1, q, std::ref(m));   // std::ref なし → q のコピーが各スレッドに渡る
    std::thread t2(worker, 2, q, std::ref(m));
    t1.join();
    t2.join();
    std::cout << "元の q に残っている個数 = " << q.size() << "\n";   // 6 のまま（誰も本物を触っていない）
    return 0;
}
