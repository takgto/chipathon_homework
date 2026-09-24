# linux_command/ ―― Linuxコマンド 事前学習用 問題集

半導体デザインハッカソン（KV260 + YOLOv3）の前に取り組む **Linux コマンドの宿題**（第1〜6章・問1〜22）です。
基本コマンドは Google Colab の確認用セルでも試せます。SSH と VS Code の章は自分の PC で行います。

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/takgto/chipathon_homework/blob/main/linux_command/linux_command_homework.ipynb) **`linux_command_homework.ipynb`**

> 💡 新しいタブで開きたいときは、バッジを `Ctrl`（Mac は `⌘`）を押しながらクリックしてください。

## 進め方

1. バッジを押して Colab を開く（「ファイル → ドライブにコピーを保存」してから使うと書き込みが残ります）
2. 各章は **解説 → 演習 → 演習の解答** の順です。**まず自分の PC のターミナルでコマンドを打ってから**解答を読んでください
3. 第1〜4章には Colab で同じコマンドを実行できる確認用セルがあります。第5・6章は自分の PC で行います

| 章 | 内容 | 問 |
|:--:|---|:--:|
| 1 | ターミナルが使えるか確認する（`whoami` / `pwd` / `ls`） | 1〜3 |
| 2 | ディレクトリを作って移動し、ファイルを整理する（`mkdir` / `cd` / `touch` / `cp` / `mv` / `rm`） | 4〜8 |
| 3 | シェルスクリプトを作って実行する（リダイレクト、`chmod +x`、`./`） | 9〜11 |
| 4 | ファイルの圧縮・展開とディスク容量の確認（`tar` / `df` / `du`） | 12〜15 |
| 5 | SSH と SCP を実際に試す（`localhost` を KV260 の代役に） | 16〜19 |
| 6 | VS Code でリモートのファイルを編集する（Remote-SSH） | 20〜22 |

## 関連

- [cpp/](../cpp) ―― C/C++ 事前学習用問題集
- [cnn/](../cnn) ―― CNN 事前学習用問題集
- [cpp-lab](https://github.com/takgto/cpp-lab) ―― C++ 並行処理演習

## リポジトリの構成

- `linux_command_homework.ipynb` ―― 問題集本体（生成物）
- `gen/build_linux.py` ―― ノートブック生成スクリプト（本文はこの中）。`python3 gen/build_linux.py` でこのフォルダ直下に再生成する

`.ipynb` は生成物です。直すときは `gen/build_linux.py` を直して再生成してください。
