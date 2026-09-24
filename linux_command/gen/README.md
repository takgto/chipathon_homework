# gen/ ―― ノートブック生成スクリプト（配布元用）

このフォルダ直下の `linux_command_homework.ipynb` はここの `build_linux.py` から生成しています。
**`.ipynb` を直接編集せず、`build_linux.py` を直して再生成してください。**

```bash
python3 gen/build_linux.py     # → linux_command_homework.ipynb（どこからでも可。追加ライブラリ不要）
```

`build_linux.py` は本文（Markdown）と確認用の `%%bash` セルをすべて自分の中に持つ自己完結スクリプトです（cpp-lab の `build.py` と同じ流儀）。
`md(...)` が Markdown セル、`code(...)` がコードセルで、上から順にセルが並びます。目次は `# 第` で始まるセルから自動生成します。
