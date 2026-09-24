# cpp/ ―― C/C++ 事前学習用 問題集

半導体デザインハッカソン（KV260 + YOLOv3）の前に取り組む **C++ の文法の宿題**（第1〜8章・問1〜25）です。
Google Colab 上で C++ をコンパイル・実行します。環境構築は要りません。

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/takgto/chipathon_homework/blob/main/cpp/cpp_homework.ipynb) **`cpp_homework.ipynb`**

> 💡 新しいタブで開きたいときは、バッジを `Ctrl`（Mac は `⌘`）を押しながらクリックしてください。

## 進め方

1. バッジを押して Colab を開く
2. **上のセルから順に ▶ を押す**
3. 各章は **解説 → 設問 → 設問の解答** の順です。**設問を自分で解いてから**解答を開いてください

| 章 | 内容 | 問 |
|:--:|---|:--:|
| 1 | コンパイルと実行、コマンドライン引数（`argc` / `argv`） | 1〜3 |
| 2 | `std::vector` | 4〜7 |
| 3 | `std::pair`・`make_pair`・`auto`・型の別名 | 8〜10 |
| 4 | 値渡し・参照渡し・ポインタと `const`（＋補足：スレッドに渡すときの `std::ref`） | 11〜14 |
| 5 | `std::chrono` で処理時間を測る | 15〜17 |
| 6 | 関数とグローバル変数・スコープ | 18〜20 |
| 7 | クラス・テンプレート・ファンクタ | 21〜22 |
| 8 | 動的メモリと `unique_ptr` | 23〜25 |

問題文で引用しているサンプルコード（`yolov3_video_series_prof.cpp` / `yolov3_video_study.cpp`）は
[cpp-lab/kv260](https://github.com/takgto/cpp-lab/tree/main/kv260) にあります。

## 関連

- [linux_command/](../linux_command) ―― Linuxコマンド 事前学習用問題集
- [cnn/](../cnn) ―― CNN 事前学習用問題集

## 続き

この問題集を終えたら、並行処理（スレッド・キュー・パイプライン）の演習 **[cpp-lab](https://github.com/takgto/cpp-lab)** へ進んでください。

## リポジトリの構成

- `cpp_homework.ipynb` ―― 問題集本体（生成物）
- `src/` ―― ノートブックが書き出す C++ ソース（`q01.cpp` …）
- `gen/build_hw.py` ―― ノートブック生成スクリプト。`python3 gen/build_hw.py` でこのフォルダ直下に `cpp_homework.ipynb` を再生成する

`.ipynb` は生成物です。直すときは `gen/build_hw.py` を直して再生成してください。
