# chipathon_homework ―― Claude Code への指示

半導体デザインハッカソン（KV260 + YOLOv3）の前に学生が取り組む **事前学習用問題集（宿題）3本** をまとめたリポジトリです。
学生が見る **public リポジトリ**（`takgto/chipathon_homework`）。続きの並行処理演習は別リポジトリ **takgto/cpp-lab** にあります。

## 構成：問題集ごとにフォルダが独立している

| フォルダ | 問題集 | 生成コマンド | 本文の置き場所 |
|---|---|---|---|
| `linux_command/` | Linux コマンド（第1〜6章・問1〜22） | `python3 linux_command/gen/build_linux.py` | `gen/build_linux.py` の中 |
| `cpp/` | C/C++（第1〜8章・問1〜25） | `python3 cpp/gen/build_hw.py` | `gen/build_hw.py` の中（コードは `src/*.cpp`） |
| `cnn/` | CNN（第1〜5章・問1〜14） | `python3 cnn/gen/build_cnn.py` | `gen/cnn_homework.md`（確認用コードは `gen/build_cnn.py`） |

- **各フォルダに専用の `CLAUDE.md` がある。そのフォルダを触る前に必ず読む**（教材の約束ごと・確認手順はそちらに書いてある）
- 生成スクリプトは自分の場所から出力先を決める（出力先は各フォルダ直下）。どこから実行してもよい。追加ライブラリは不要（cnn の図の PNG 化だけ Playwright が要る）
- フォルダをまたいでファイルを共有していない。1つの問題集の変更で他のフォルダを触る必要は基本的にない

```
chipathon_homework/
├── README.md          学生向けトップ。3問題集の Colab バッジと進め方
├── CLAUDE.md          このファイル
├── linux_command/     README.md, CLAUDE.md, linux_command_homework.ipynb, gen/
├── cpp/               README.md, CLAUDE.md, cpp_homework.ipynb, src/, gen/
└── cnn/               README.md, CLAUDE.md, cnn_homework.ipynb, img/, gen/
```

## 最重要ルール：`.ipynb` は生成物。直接編集しない

- 3本とも `gen/` のスクリプトから生成している。直すときは生成元を直して **再生成** する（`.ipynb` を直接直すと次の再生成で消える）
- Colab で実行結果（outputs）が入った `.ipynb` を commit しない
- 変更後は該当フォルダで再生成し、`git diff --stat` で **想定したファイルだけ** が変わっていることを確認する。生成元を触っていないフォルダの `.ipynb` に差分が出たらおかしい

## 3本で揃えていること（どれかを変えるときは他も確認する）

- 章の見出し階層：`# 第N章　…`（全角スペース）→ `## 解説` → `---` → `## 演習` / `## 設問` → `### 問N` → `## 演習の解答` / `## 設問の解答` → `### 問N`（linux は「演習」、cpp / cnn は「設問」）
- 問の番号は章をまたいで通し番号。設問と解答で同じ番号
- 目次は `# 第` で始まるセルから自動生成し、`#scrollTo=<ノートブック名>_NN` でリンクする
- 各フォルダの `README.md` は「Colab バッジ → 💡新しいタブ → 進め方 → 章と問の表 → 関連 → リポジトリの構成」の順

## README とリンク

- Colab リンクは必ず **`https://colab.research.google.com/github/takgto/chipathon_homework/blob/main/<フォルダ>/<ノートブック>.ipynb`** の形式（ブランチは `main`）
- トップの `README.md` は cpp-lab の README の形式（表：バッジ＋問題集名 ／ 学ぶこと、進め方、注意書きの引用ブロック）に合わせてある
- 章や問を増減したら、**各フォルダの README の表と、トップ README の「第N〜M章・問1〜K」の両方** を直す
- フォルダ間のリンクは相対パス（`../cpp` など）。cpp-lab へは `https://github.com/takgto/cpp-lab`

## Git の扱い

- 環境：Windows 上の WSL2（Ubuntu 20.04）。ブランチは `main`
- commit は自由に行ってよい。commit メッセージは日本語でよい
- **push は行う前に一度確認を取る**（学生が見る public リポジトリのため）
- `__pycache__/`（全フォルダ）、`cnn/data/`（MNIST のダウンロード先）は各フォルダの `.gitignore` で除外済み
- `CLAUDE.md` も公開される。個人の環境情報（Windows のユーザー名やローカルのパスなど）を書き込まない
