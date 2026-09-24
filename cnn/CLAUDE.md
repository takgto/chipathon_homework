# cnn-homework ―― Claude Code への指示

半導体デザインハッカソン（KV260 + YOLOv3）の前に学生が取り組む **CNN 事前学習用問題集**（第1〜5章、問1〜問14）です。
第4章は Google Colab 上で LeNet を学習・推論します。姉妹リポジトリ：**takgto/cpp-homework**（C/C++ 問題集）、**takgto/cpp-lab**（C++ 並行処理演習）。

## 最重要ルール：`.ipynb` は生成物。直接編集しない

- `cnn_homework.ipynb` は **`gen/build_cnn.py` が `gen/cnn_homework.md` から生成** している
- 本文を直すときは **`gen/cnn_homework.md`** を直す。確認用コード・第4章のコードを直すときは **`gen/build_cnn.py`** を直す。どちらも直したら **再生成** する
- `.ipynb` を直接編集してはいけない（次の再生成で消える）
- Colab で実行結果（outputs。特に MNIST の学習ログや画像）が入った `.ipynb` を commit しない

```bash
python3 gen/build_cnn.py     # リポジトリのどこからでも可。出力先はリポジトリ直下。追加ライブラリ不要
```

## 変更したときの確認手順

1. `python3 gen/build_cnn.py` で再生成し、`git diff --stat` で `cnn_homework.ipynb` だけが変わっていることを確認する
2. `cnn_homework.md` の見出し構造（下記）を崩していないこと。崩すと `build_cnn.py` の `assert`（解答14問・設問14問）で止まる
3. 確認用コード（問1・3・6・13）は torch 不要なので、`python3 -c` で単体実行して通ることを確認する。第4章と問9・10のコードは torch が要るので、Colab で実行して確認する
4. 図を変えたときは `python3 gen/figs/render.py` で `img/` を更新してから再生成する（Playwright が必要。無ければ SVG だけ直して、PNG 更新は人に頼む）

## ディレクトリ構成

```
cnn-homework/
├── README.md              学生向け。Colab バッジ、章と問の一覧
├── CLAUDE.md              このファイル
├── .gitignore
├── cnn_homework.ipynb     問題集本体（生成物。図は base64 で埋め込み済み、約1.5MB）
├── img/                   ノートブックに埋め込む図（PNG 8枚。gen/figs/render.py の出力）
└── gen/
    ├── README.md
    ├── build_cnn.py       生成スクリプト（確認用コードと第4章のコードもこの中）
    ├── cnn_homework.md    本文の原稿
    └── figs/
        ├── svg/*.svg      図の元データ
        ├── make_bbox.py, make_lenet.py   SVG を描くスクリプト
        └── render.py      SVG → ../img/*.png（Playwright）
```

## `cnn_homework.md` の構造（`build_cnn.py` が正規表現で拾う）

```
# CNN 事前学習用 問題集（宿題）      ← 冒頭（ノートブックでは build_cnn.py 側の文章に差し替わる）
# 第N章　…                          ← 章（N = 1〜5）
## 解説
## 設問
**問N.** …                         ← 通し番号。全体で 1〜14
# 解答編
## 問Nの解答                        ← 1〜14 すべて必要
## まとめ
```

- 図は `![説明](figures/xxx.svg)` と書く。生成時に `img/xxx.png` の base64 埋め込み `<img>` に置き換わる。幅は `build_cnn.py` の `FIG_W` で決める
- 第4章の解説にある `**Colabでの進め方**` より後ろは、ノートブックでは捨てて `build_cnn.py` 側のセル分割コードに置き換える

## 教材の約束ごと（変更するときに守る）

- 見出しの階層は 3 つの問題集（linux / cpp / cnn）で共通：`# 第N章　…` → `## 解説` → `---` → `## 設問` → `### 問N`（各設問）→ `## 設問の解答` → `### 問N`（各解答）。第4章だけ 解説 と 設問 の間に `## 演習コード（PyTorch）` が入る
- 問の番号は章をまたいで通し（問1〜14）。設問と解答で同じ番号を使う
- 対象は「機械学習を少しかじった学生」。記号は `W`（入力一辺）、`K`（カーネル）、`S`（ストライド）、`P`（パディング）、`Cin` / `Cout` で統一
- 出力サイズの公式は `O = ⌊(W − K + 2P) / S⌋ + 1`。数値例を変えるときは確認用コードも合わせる
- 第4章の LeNet は 3 エポックで test accuracy 98〜99% になる設定。`EPOCHS` を変える演習（問10）があるので、コードの変数名を変えない
- 第5章の YOLOv3 の数値（416 入力、13/26/52 グリッド、アンカー3、80 クラス、`3×(5+80)=255` チャネル、候補枠 10,647）は本番の KV260 コードと対応している。変えない
- 図番号と本文の対応（図1〜図8）を崩さない

## Git の扱い

- commit は自由に行ってよい。commit メッセージは日本語でよい
- **push は行う前に一度確認を取る**（学生が見る public リポジトリのため）
- `__pycache__/`、`data/`（MNIST のダウンロード先）は `.gitignore` 済み

## 初回セットアップ（完了したらこの節は削除してよい）

- 環境：Windows 上の WSL2。zip は Windows 側の Downloads にあり、WSL2 からは **`/mnt/c/Users/kurod/Downloads/cnn_homework_gen.zip`**（見つからなければ聞くこと）
- GitHub に空の public リポジトリ（例：`takgto/cnn-homework`）を作って clone した直後の状態を想定

1. clone したリポジトリ直下で `unzip -o /mnt/c/Users/kurod/Downloads/cnn_homework_gen.zip` を実行する
2. リポジトリ名が `cnn-homework` でない場合、`README.md` の Colab バッジ URL 中の `cnn-homework` を実際の名前に直す
3. `python3 gen/build_cnn.py` を実行し、`git status` で `cnn_homework.ipynb` に差分が出ないことを確認する
4. `git add .` → commit
5. push は確認を取ってから。push 後、README のバッジから Colab が開き、図が表示され、第4章が最後まで実行できることを確認する
