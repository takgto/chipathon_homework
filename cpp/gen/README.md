# gen/ ―― ノートブック生成スクリプト（配布元用）

このフォルダ直下の `cpp_homework.ipynb` はここの `build_hw.py` から生成しています。
**`.ipynb` を直接編集せず、`build_hw.py`（本文）か `../src/*.cpp`（コード）を直して再生成してください。**

```bash
# どこからでも実行できる（出力先はこのフォルダ直下）
python3 gen/build_hw.py      # → cpp_homework.ipynb
```

| ファイル | 役割 |
|---|---|
| `build_hw.py` | 本文（Markdown）とセルの並びを持つ生成スクリプト。cpp-lab の `gen/build.py` と同じ流儀で、自己完結している |
| `../src/qNN*.cpp` | ノートブックが `%%writefile` で書き出す C++ ソース。`src('q02.cpp', 'ans2.cpp')` のように **リポジトリ内の名前 → ノートブック上の名前** を対応づけている |

`src/` の命名：`qNN_try.cpp` = 第N章の設問で学生が書き込む骨組み、`qNN.cpp` / `qNNa.cpp`… = 解答。
セルの目次リンク（`#scrollTo=cpp_homework_NN`）は `build_hw.py` が見出しセルの位置から自動で振るので、セルを増減しても手で直す必要はありません。
