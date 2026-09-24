# cnn/ ―― CNN 事前学習用 問題集

半導体デザインハッカソン（KV260 + YOLOv3）の前に取り組む **CNN の基礎の宿題** です。
第4章では Google Colab 上で LeNet を学習・推論します。環境構築は要りません。

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/takgto/chipathon_homework/blob/main/cnn/cnn_homework.ipynb) **`cnn_homework.ipynb`**

> 💡 新しいタブで開きたいときは、バッジを `Ctrl`（Mac は `⌘`）を押しながらクリックしてください。

## 進め方

1. バッジを押して Colab を開く（「ファイル → ドライブにコピーを保存」してから使うと書き込みが残ります）
2. 各章は **解説 → 設問 → 設問の解答** の順です。**設問を自分で考えてから**解答を読んでください
3. 第4章のコードセルは **上から順に ▶ を押す**。GPU（T4 など）を選ぶと速いですが、CPU でも数分で終わります

| 章 | 内容 | 問 |
|:--:|---|:--:|
| 1 | CNN の基礎（畳み込み、出力サイズの公式、パラメータ共有） | 1〜3 |
| 2 | Encoder-Decoder（U-Net、スキップ接続） | 4〜5 |
| 3 | いろいろな畳み込み（グループ化・深さ方向分離） | 6〜8 |
| 4 | LeNet で MNIST を学習する（Colab 演習） | 9〜10 |
| 5 | YOLOv3 のネットワーク構造での CNN（残差、FPN、出力テンソル） | 11〜14 |

## 関連

- [linux_command/](../linux_command) ―― Linuxコマンド 事前学習用問題集
- [cpp/](../cpp) ―― C/C++ 事前学習用問題集
- [cpp-lab](https://github.com/takgto/cpp-lab) ―― C++ 並行処理演習（スレッド・キュー・パイプライン）

## リポジトリの構成

- `cnn_homework.ipynb` ―― 問題集本体（生成物）
- `img/` ―― ノートブックに埋め込む図（PNG）
- `gen/build_cnn.py` ―― ノートブック生成スクリプト。`python3 gen/build_cnn.py` でこのフォルダ直下に `cnn_homework.ipynb` を再生成する
- `gen/cnn_homework.md` ―― 本文の原稿（`build_cnn.py` が読む）
- `gen/figs/` ―― 図の生成元（SVG と作図スクリプト）

`.ipynb` は生成物です。直すときは `gen/cnn_homework.md` を直して再生成してください。
