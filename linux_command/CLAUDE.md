# linux-homework ―― Claude Code への指示

半導体デザインハッカソン（KV260 + YOLOv3）の前に学生が取り組む **Linux コマンド 事前学習用問題集**（第1〜6章・問1〜22）です。
姉妹リポジトリ：**takgto/cpp-homework**（C/C++）、**takgto/cnn-homework**（CNN）、**takgto/cpp-lab**（C++ 並行処理演習）。

## 最重要ルール：`.ipynb` は生成物。直接編集しない

- `linux_command_homework.ipynb` は **`gen/build_linux.py` から生成** している。本文も確認用セルもこのスクリプトの中にある
- 直すときは `gen/build_linux.py` を直して **再生成** する。`.ipynb` を直接編集してはいけない（次の再生成で消える）
- Colab で実行結果（outputs）が入った `.ipynb` を commit しない

```bash
python3 gen/build_linux.py     # リポジトリのどこからでも可。出力先はリポジトリ直下。追加ライブラリ不要
```

## 変更したときの確認手順

1. `python3 gen/build_linux.py` で再生成し、`git diff --stat` で `linux_command_homework.ipynb` だけが変わっていることを確認する
2. `%%bash` セルを変えたときは、`HOME` を一時ディレクトリに向けて bash で実行し、通ることを確認する（第2〜4章のセルは `~/practice` を作る・消すので、本物の `HOME` で試さない）

## ディレクトリ構成

```
linux-homework/
├── README.md                     学生向け。Colab バッジ、章と問の一覧
├── CLAUDE.md                     このファイル
├── .gitignore
├── linux_command_homework.ipynb  問題集本体（生成物）
└── gen/
    ├── README.md
    └── build_linux.py            生成スクリプト（本文はこの中）
```

## 教材の約束ごと（変更するときに守る）

- 見出しの階層は 3 つの問題集（linux / cpp / cnn）で共通：`# 第N章　…`（全角スペース）→ `## 解説` → `---` → `## 演習` → `### 問N`（各演習）→ `## 演習の解答` → `### 問N`（各解答）
- 問の番号は **章をまたいで通し**（第1章 問1〜3、第2章 問4〜8、第3章 問9〜11、第4章 問12〜15、第5章 問16〜19、第6章 問20〜22）。演習と解答で同じ番号を使う。増減したら後ろを全部ずらす（README の「問」列も）
- 各章の確認用 `%%bash` セルは「演習の解答」の最後に 1 つ（第1〜4章のみ）。第5・6章（SSH / VS Code）は Colab で試せないので確認用セルを置かない
- 「解説」には元の「シーン」と、章に必要な準備手順（第5章の SSH サーバー、第6章の VS Code）を入れる。ヒントは「演習」の末尾
- `localhost` を KV260 の代役にする、という考え方を第5・6章で崩さない。本番のアドレス例は `root@192.168.1.100`
- 対象は「Linux を少し触ったことがある学生」。WSL2（Ubuntu 20.04）と Mac の両方で動くコマンドだけを使う

## Git の扱い

- commit は自由に行ってよい。commit メッセージは日本語でよい
- **push は行う前に一度確認を取る**（学生が見る public リポジトリのため）
- `__pycache__/` は `.gitignore` 済み

## 初回セットアップ（完了したらこの節は削除してよい）

- 環境：Windows 上の WSL2。zip は Windows 側の Downloads にあり、WSL2 からは **`/mnt/c/Users/kurod/Downloads/linux_command_homework_gen.zip`**（見つからなければ聞くこと）
- GitHub に空の public リポジトリ（例：`takgto/linux-homework`）を作って clone した直後の状態を想定

1. clone したリポジトリ直下で `unzip -o /mnt/c/Users/kurod/Downloads/linux_command_homework_gen.zip` を実行する
2. リポジトリ名が `linux-homework` でない場合、`README.md` の Colab バッジ URL 中の `linux-homework` を実際の名前に直す
3. `python3 gen/build_linux.py` を実行し、`git status` で `linux_command_homework.ipynb` に差分が出ないことを確認する
4. `git add .` → commit
5. push は確認を取ってから。push 後、README のバッジから Colab が開き、第1〜4章の確認用セルが通ることを確認する
