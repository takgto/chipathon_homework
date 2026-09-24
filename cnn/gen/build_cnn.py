#!/usr/bin/env python3
"""CNN 事前学習用 問題集 → Google Colab 用 ipynb 生成スクリプト（cpp-lab の build.py と同じ流儀）
構成：章ごとに 解説 → (問N → 問Nの解答) … 。計算問題の解答には確認用コードセルを付ける。
第4章（LeNet/MNIST）はコードを段階ごとのセルに分割し、ノートブック上でそのまま実行できるようにする。

  読み込み：gen/cnn_homework.md（本文の原稿）、img/*.png（図）
  出力    ：リポジトリ直下の cnn_homework.ipynb
  実行    ：python3 gen/build_cnn.py（リポジトリのどこからでも可。追加ライブラリ不要）
"""
import re, base64, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent                                  # リポジトリ直下
SRC  = HERE / "cnn_homework.md"                     # 本文の原稿
PNG  = ROOT / "img"                                 # 図（gen/figs/ で生成した PNG）
NAME = "cnn_homework"
OUT  = ROOT / f"{NAME}.ipynb"

md = SRC.read_text(encoding="utf-8")

# ---------- 図の埋め込み（PNG を base64 の data URI に） ----------
FIG_W = {"cnn_vs_fc": 760, "cnn_unet": 760, "cnn_lenet": 760, "cnn_bbox": 760, "cnn_conv": 760, "cnn_residual": 600, "cnn_yolov3": 600, "cnn_yolov3_tiny": 600}

def fig_tag(stem):
    b64 = base64.b64encode((PNG / f"{stem}.png").read_bytes()).decode()
    return f'<img src="data:image/png;base64,{b64}" width="{FIG_W[stem]}">'

def embed_figs(text):
    return re.sub(r"!\[[^\]]*\]\(figures/(\w+)\.svg\)", lambda m: fig_tag(m.group(1)), text)

# ---------- 元 md のパース ----------
# 章：「# 第N章 …」から次の「# 」まで
chapters = {}
for m in re.finditer(r"^# (第(\d)章[^\n]*)\n(.*?)(?=^# 第|^# 解答編|\Z)", md, re.S | re.M):
    title, num, body = m.group(1), int(m.group(2)), m.group(3)
    kaisetsu = re.search(r"^## 解説\n(.*?)(?=^## 設問)", body, re.S | re.M).group(1).strip()
    setsumon = re.search(r"^## 設問\n(.*?)(?=^---\s*$|\Z)", body, re.S | re.M).group(1).strip()
    qs = {}
    for q in re.finditer(r"\*\*問(\d+)\.\*\*(.*?)(?=\*\*問\d+\.\*\*|\Z)", setsumon, re.S):
        qs[int(q.group(1))] = q.group(2).strip()
    chapters[num] = dict(title=title, kaisetsu=kaisetsu, qs=qs)

answers = {}
kaitou = re.search(r"^# 解答編\n(.*?)(?=^---\s*$\n\n## まとめ)", md, re.S | re.M).group(1)
for a in re.finditer(r"^## 問(\d+)の解答\n(.*?)(?=^## 問\d+の解答|\Z)", kaitou, re.S | re.M):
    answers[int(a.group(1))] = a.group(2).strip()

osarai = re.search(r"^## まとめ.*", md, re.S | re.M).group(0).strip()

assert set(answers) == set(range(1, 15)), sorted(answers)
assert sum(len(c["qs"]) for c in chapters.values()) == 14

# ---------- ノートブック組み立て ----------
cells = []
def _lines(text):
    """nbformat の source 形式：各行の末尾に \n（最終行だけは付けない）"""
    ls = text.strip("\n").split("\n")
    return [l + "\n" for l in ls[:-1]] + [ls[-1]]
def MD(s):   cells.append({"cell_type": "markdown", "metadata": {}, "source": _lines(s)})
def CODE(s): cells.append({"cell_type": "code", "execution_count": None, "metadata": {},
                           "outputs": [], "source": _lines(s)})

# --- 冒頭 ---
MD(r"""
# CNN 事前学習用 問題集（宿題）

半導体デザインハッカソンでは、FPGAを搭載した評価ボード（KV260）を使って物体検出を行います。ここでは深層学習で最も大事な構成要素であるCNN（Convolutional Neural Network、畳み込みニューラルネットワーク）の基礎、及びKV260の物体検出に用いられるYOLOv3のネットワーク構成と原理についても演習を通じて学びます。

- **対象レベル**：機械学習を少しかじったことがある人。知らない用語は **検索しながら** で構いません。
- **使い方**：各章は「**解説**」→「**設問**」→「**設問の解答**」の順です。まず解説を読み、設問を自分で考えてから、解答で答え合わせをします。**解答はスクロールするとすぐ見えてしまうので、先に自分で考えてから読み進めてください。**
- **手を動かす章**：第4章はこのノートブック上で実際にCNN（LeNet）を学習・推論します。コードセルを上から順に ▶ で実行してください。**ブラウザだけ** で動き、PCへのインストールは不要です。
- **確認用セル**：計算問題（問1・3・6・9・13）の解答には、答えをPythonで計算する確認用セルを付けています。自分の計算と突き合わせてみてください。
- **このノートブックの使い方**：メニュー「ファイル → ドライブにコピーを保存」で自分のGoogleドライブにコピーしてから使うと、書き込んだ内容が保存されます。左側の目次（≡）から各章・各問に移動できます。
- **記号の約束**：本書では、入力画像の一辺を `W`、フィルタの一辺を `K`、ストライド（フィルタをずらす歩幅・後述）を `S`、パディング（入力の周囲を広げる量・後述）を `P`、入力チャネル数を `Cin`、出力チャネル数（フィルタの枚数）を `Cout` と書きます。（`S` と `P` は第1章で解説します。）
""")

# --- 確認用コード（問番号 → コード） ---
CHECK = {
1: r'''
# 問1の確認：出力サイズ公式 O = floor((W - K + 2P) / S) + 1
def out_size(W, K, P, S):
    return (W - K + 2 * P) // S + 1

W, K = 28, 5
for P, S in [(0, 1), (2, 1), (0, 2)]:
    O = out_size(W, K, P, S)
    print(f"P={P}, S={S}:  O = floor(({W} - {K} + 2*{P}) / {S}) + 1 = {O}  ->  {O}x{O}")
''',
3: r'''
# 問3の確認：畳み込み層と全結合層のパラメータ数
K, Cin, Cout = 3, 3, 16
conv_params = (K * K * Cin + 1) * Cout
print(f"畳み込み層 : (K*K*Cin + 1) * Cout = ({K}*{K}*{Cin} + 1) * {Cout} = {conv_params:,}")

n_in  = 32 * 32 * 3
n_out = 32 * 32 * 16
fc_weights = n_in * n_out
print(f"全結合層   : {n_in:,} x {n_out:,} = {fc_weights:,} 個の重み（バイアス除く）")
print(f"比         : 全結合 / 畳み込み ≈ {fc_weights / conv_params:,.0f} 倍")
''',
6: r'''
# 問6の確認：標準畳み込み vs depthwise + pointwise
K, M, N = 3, 32, 64
standard  = K * K * M * N
depthwise = K * K * M
pointwise = M * N
separable = depthwise + pointwise
print(f"(a) 標準畳み込み      : {K}*{K}*{M}*{N} = {standard:,}")
print(f"(b) depthwise {depthwise} + pointwise {pointwise:,} = {separable:,}")
print(f"(c) 標準 / 分離 = {standard / separable:.2f} 倍軽い")
print(f"    公式 1/N + 1/K^2 = 1/{N} + 1/{K*K} = {1/N + 1/(K*K):.4f} （≈ 1/{1/(1/N + 1/(K*K)):.1f}）")
''',
13: r'''
# 問13の確認：最も粗いスケールの出力テンソルの形
W_in, stride_total = 416, 32
B, C = 3, 80
grid = W_in // stride_total
ch = B * (5 + C)
print(f"グリッド  : {W_in} / {stride_total} = {grid}  ->  {grid}x{grid}")
print(f"チャネル  : B * (5 + C) = {B} * (5 + {C}) = {ch}")
print(f"出力テンソル : {grid} x {grid} x {ch}")
n_boxes = sum(g * g for g in (13, 26, 52)) * B
print(f"3スケール合計の候補枠 : (13*13 + 26*26 + 52*52) * {B} = {n_boxes:,}")
''',
}

def emit_questions(ns):
    """## 設問 の下に ### 問N を並べる（3 つの問題集で共通の見出し階層）"""
    MD("---\n\n## 設問")
    for n in ns:
        MD(f"### 問{n}\n\n{chapters[chap]['qs'][n]}")

def emit_answers(ns):
    """## 設問の解答 の下に ### 問N を並べる。計算問題には確認用コードを付ける"""
    MD("## 設問の解答")
    for n in ns:
        MD(f"### 問{n}\n\n{answers[n]}")
        if n in CHECK:
            CODE(CHECK[n])

# --- 第1〜3章 ---
for chap in (1, 2, 3):
    c = chapters[chap]
    MD(f"# {c['title']}")
    MD("## 解説\n\n" + embed_figs(c["kaisetsu"]))
    emit_questions(sorted(c["qs"]))
    emit_answers(sorted(c["qs"]))

# --- 第4章（コードをセルに分割） ---
chap = 4
c = chapters[4]
MD(f"# {c['title']}")
k4 = c["kaisetsu"].split("**Colabでの進め方**")[0].strip()
MD("## 解説\n\n" + embed_figs(k4))
MD(r"""
**進め方**：下のコードセルを **上から順に** ▶（実行）で実行してください。

- （任意）メニュー「ランタイム → ランタイムのタイプを変更」で **GPU**（T4など）を選ぶと速いです。CPUのままでも数分で終わります。
- 学習（3エポック）は GPU で 30秒〜1分、CPU で 2〜3分程度です。
- PyTorch と torchvision は Colab に最初から入っているので、インストールは不要です。
""")
MD("## 演習コード（PyTorch）\n\n### (1) 準備：ライブラリの読み込みとデバイスの確認\n\nGPUが使えれば `cuda`、使えなければ `cpu` と表示されます。")
CODE(r'''
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

device = "cuda" if torch.cuda.is_available() else "cpu"
print("device =", device)
''')
MD("### (2) データ準備（MNIST：初回は自動ダウンロード）\n\n学習用6万枚・テスト用1万枚の `28×28` グレースケール画像を読み込みます。")
CODE(r'''
transform = transforms.ToTensor()
train_ds = datasets.MNIST(root="./data", train=True,  download=True, transform=transform)
test_ds  = datasets.MNIST(root="./data", train=False, download=True, transform=transform)
train_loader = DataLoader(train_ds, batch_size=128, shuffle=True)
test_loader  = DataLoader(test_ds,  batch_size=256)

print("train:", len(train_ds), "枚   test:", len(test_ds), "枚")
img, label = train_ds[0]
print("1枚の形 (チャネル×高さ×幅):", tuple(img.shape), "  ラベル:", label)
''')
MD("### (3) LeNet の定義\n\n解説の構造図と、コードのコメント（各層を通ったあとの形）を対応づけて読んでください。")
CODE(r'''
class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 6, kernel_size=5, padding=2)  # 1x28x28 -> 6x28x28
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5)            # 6x14x14 -> 16x10x10
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)  # -> 6x14x14
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)  # -> 16x5x5
        x = x.view(x.size(0), -1)                   # -> 400
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)                          # -> 10

model = LeNet().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

print(model)
print("学習パラメータ数:", sum(p.numel() for p in model.parameters()))
''')
MD("### (4) 学習（3エポックでも十分高精度）\n\n`EPOCHS` の値を変えると学習の回数を変えられます（問10で使います）。")
CODE(r'''
EPOCHS = 3

for epoch in range(EPOCHS):
    model.train()
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        optimizer.step()
    print(f"epoch {epoch + 1} done, last loss = {loss.item():.4f}")
''')
MD("### (5) テストデータで精度を測る\n\nうまくいけば、テスト精度はおよそ **98〜99%** になります。")
CODE(r'''
model.eval()
correct = 0
with torch.no_grad():
    for x, y in test_loader:
        x, y = x.to(device), y.to(device)
        pred = model(x).argmax(dim=1)
        correct += (pred == y).sum().item()
print(f"test accuracy = {100 * correct / len(test_ds):.2f}%")
''')
MD("### (6) 1枚だけ推論して画像と一緒に表示\n\n`idx` を変えると別の画像を試せます。")
CODE(r'''
import matplotlib.pyplot as plt

idx = 0
img, label = test_ds[idx]
model.eval()
with torch.no_grad():
    pred = model(img.unsqueeze(0).to(device)).argmax(dim=1).item()
plt.imshow(img.squeeze(), cmap="gray")
plt.title(f"prediction = {pred}, label = {label}")
plt.axis("off")
plt.show()
''')

emit_questions([9, 10])
MD("## 設問の解答")
MD(f"### 問9\n\n{answers[9]}")
CODE(r'''
# 問9の確認：実際のテンソルの形を各段階で表示する（(3) の model を使う）
x = torch.zeros(1, 1, 28, 28).to(device)   # バッチサイズ1のダミー入力
print("入力            :", tuple(x.shape[1:]))
x = F.relu(model.conv1(x));  print("conv1           :", tuple(x.shape[1:]))
x = F.max_pool2d(x, 2);      print("max pool 2x2    :", tuple(x.shape[1:]))
x = F.relu(model.conv2(x));  print("conv2           :", tuple(x.shape[1:]))
x = F.max_pool2d(x, 2);      print("max pool 2x2    :", tuple(x.shape[1:]))
x = x.view(x.size(0), -1);   print("flatten         :", x.shape[1], "要素")
x = model.fc1(x);            print("fc1             :", x.shape[1])
x = model.fc2(x);            print("fc2             :", x.shape[1])
x = model.fc3(x);            print("fc3 (出力)      :", x.shape[1])
''')
MD(f"### 問10\n\n{answers[10]}\n\n下のセルで、モデルを作り直して **1エポックだけ** 学習し、精度を比べてみてください（(4) の `EPOCHS = 1` に変えて (3)〜(5) を実行し直しても同じことができます）。")
CODE(r'''
# 問10(b) の確認：エポック数を変えて学習し直す
def train_and_eval(epochs, seed=0):
    torch.manual_seed(seed)
    m = LeNet().to(device)
    opt = torch.optim.Adam(m.parameters(), lr=1e-3)
    for epoch in range(epochs):
        m.train()
        for x, y in train_loader:
            x, y = x.to(device), y.to(device)
            opt.zero_grad()
            loss = loss_fn(m(x), y)
            loss.backward()
            opt.step()
    m.eval()
    correct = 0
    with torch.no_grad():
        for x, y in test_loader:
            x, y = x.to(device), y.to(device)
            correct += (m(x).argmax(dim=1) == y).sum().item()
    return 100 * correct / len(test_ds)

for ep in (1, 3):
    print(f"epochs = {ep}: test accuracy = {train_and_eval(ep):.2f}%")
''')

# --- 第5章 ---
chap = 5
c = chapters[5]
MD(f"# {c['title']}")
MD("## 解説\n\n" + embed_figs(c["kaisetsu"]))
emit_questions(sorted(c["qs"]))
emit_answers(sorted(c["qs"]))

# --- おさらい ---
MD(osarai)

# セルごとに id を振る（Colab の #scrollTo= アンカー用。cpp-lab と同じ規則）
for i, c in enumerate(cells):
    c["metadata"]["id"] = f"{NAME}_{i:02d}"
nb = {
    "nbformat": 4, "nbformat_minor": 0,
    "metadata": {
        "colab": {"provenance": [], "toc_visible": True},
        "kernelspec": {"display_name": "Python 3", "name": "python3"},
        "language_info": {"name": "python"},
    },
    "cells": cells,
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("wrote", OUT.name, "cells:", len(cells), "code:", sum(1 for x in cells if x["cell_type"] == "code"))
