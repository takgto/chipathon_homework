# chipathon_homework

**半導体デザインハッカソン（KV260 + YOLOv3）の事前学習用 問題集（宿題）です。**
3つとも Google Colab で開けます。環境構築は要りません（Linux コマンドの SSH・VS Code の章だけは自分の PC で行います）。

---

## 問題集（宿題）

バッジを押すと Colab が開きます。**上のセルから順に読み進め、解答を見る前に自分で解いて**ください。

| | 問題集 | 学ぶこと |
|---|---|---|
| **1** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/takgto/chipathon_homework/blob/main/linux_command/linux_command_homework.ipynb) **Linux コマンド**（第1〜6章・問1〜22） | `whoami` / `pwd` / `ls`、ファイル操作、`chmod +x` と `./`、`tar` / `df` / `du`、`ssh` / `scp`、VS Code Remote-SSH |
| **2** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/takgto/chipathon_homework/blob/main/cpp/cpp_homework.ipynb) **C/C++**（第1〜8章・問1〜25） | コンパイルと `argc` / `argv`、`std::vector`、`pair` と `auto`、値渡し・参照・ポインタ、`std::chrono`、スコープ、クラスとテンプレート、`unique_ptr` |
| **3** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/takgto/chipathon_homework/blob/main/cnn/cnn_homework.ipynb) **CNN**（第1〜5章・問1〜14） | 畳み込みと出力サイズ、U-Net とスキップ接続、グループ化・深さ方向分離畳み込み、LeNet で MNIST を学習、YOLOv3 の構造（残差・FPN・出力テンソル） |

> 💡 新しいタブで開きたいときは、バッジを `Ctrl`（Mac は `⌘`）を押しながらクリックしてください。

### 進め方

1. バッジを押して Colab を開く（「**ファイル → ドライブにコピーを保存**」してから使うと、書き込んだ内容が残ります）
2. 各章は **解説 → 演習（設問） → 解答** の順に並んでいます
3. **解答を読む前に、必ず自分で解く** ―― 解答はスクロールするとすぐ見えてしまうので注意してください

> 🖥 **Linux コマンド**の第5・6章（SSH / VS Code）は Colab では試せません。自分の PC（Windows は WSL2 の Ubuntu、Mac はターミナル）で行います。
> 第1〜4章は Colab の確認用セルでも試せますが、**自分の PC のターミナルでも必ず打って**ください。

> ⏱ **CNN** の第4章（LeNet の学習）は、ランタイムで GPU（T4 など）を選ぶと速く終わります。CPU でも数分で終わります。

---

## 続き

問題集を終えたら、C++ の並行処理（スレッド・キュー・パイプライン）の演習 **[cpp-lab](https://github.com/takgto/cpp-lab)** へ進んでください。

---

## リポジトリの構成

問題集ごとにフォルダを分けています。各フォルダの `README.md` に詳しい説明があります。

- [`linux_command/`](linux_command) ―― Linux コマンド 事前学習用 問題集（`linux_command_homework.ipynb`）
- [`cpp/`](cpp) ―― C/C++ 事前学習用 問題集（`cpp_homework.ipynb`、`src/` に C++ ソース）
- [`cnn/`](cnn) ―― CNN 事前学習用 問題集（`cnn_homework.ipynb`、`img/` に図）

各フォルダの `gen/` はノートブック生成スクリプト（配布元用）です。
`.ipynb` は生成物です。**Colab や Jupyter で直接直しても、次の配布で上書きされます。**
誤りや改善点は配布元までご連絡ください。
