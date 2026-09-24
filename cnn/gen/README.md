# gen/ ―― ノートブック生成スクリプト（配布元用）

このフォルダ直下の `cnn_homework.ipynb` はここの `build_cnn.py` から生成しています。
**`.ipynb` を直接編集せず、原稿 `cnn_homework.md` を直して再生成してください。**

```bash
# どこからでも実行できる（出力先はこのフォルダ直下）。追加ライブラリは不要
python3 gen/build_cnn.py     # → cnn_homework.ipynb
```

| ファイル | 役割 |
|---|---|
| `build_cnn.py` | `cnn_homework.md` を章・設問・解答に分解し、「解説 → 問N → 問Nの解答（＋確認用コード）」の順に並べ直して `.ipynb` にする。第4章の LeNet コードはセルに分割して埋め込む。確認用コード（問1・3・6・9・10・13）は **このスクリプトの中**（`CHECK` と第4章の `CODE(...)`）にある |
| `cnn_homework.md` | 本文の原稿。**構造が決まっている**：`# 第N章 …` → `## 解説` → `## 設問`（`**問N.**` で始める）、末尾に `# 解答編` → `## 問Nの解答`、`## まとめ`。この見出しを `build_cnn.py` が正規表現で拾うので、書式を変えない。図は `![…](figures/xxx.svg)` と書く（生成時に `img/xxx.png` の埋め込みに置き換わる） |
| `figs/svg/*.svg` | 図の元データ（8枚） |
| `figs/make_bbox.py`, `figs/make_lenet.py` | SVG を Python で描くスクリプト（`figs/svg/` に書き出す）。他の SVG は手描き |
| `figs/render.py` | `figs/svg/*.svg` → `../img/*.png`（2倍解像度）。Playwright + Chromium が必要：`pip install playwright && playwright install chromium` |

図を直す手順：SVG（または `make_*.py`）を直す → `python3 gen/figs/render.py` で `img/` の PNG を更新 → `python3 gen/build_cnn.py` で再生成。
