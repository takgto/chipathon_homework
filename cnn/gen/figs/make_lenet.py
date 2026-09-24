o=[]; A=o.append
W,H=760,360
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Noto Sans CJK JP, sans-serif">')
A('<defs><marker id="ab" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#2563eb"/></marker>'
  '<marker id="ap" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#7c3aed"/></marker></defs>')
A('<text x="380" y="26" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e3a8a">LeNet の全体構造（入力 1×28×28 → 出力 10）</text>')
def box(x,y,w,h,fill,stroke,tc,lines,fs=12):
    A(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    n=len(lines); cy=y+h/2-(n-1)*8
    for i,(t,b) in enumerate(lines):
        fw=' font-weight="bold"' if b else ''
        A(f'<text x="{x+w/2}" y="{cy+i*16+4}" text-anchor="middle" font-size="{fs}"{fw} fill="{tc}">{t}</text>')
def arrow(x1,y1,x2,y2,label=None,ly=None,lx=None):
    A(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#2563eb" stroke-width="2" marker-end="url(#ab)"/>')
    if label:
        for j,t in enumerate(label):
            A(f'<text x="{lx}" y="{ly+j*13}" text-anchor="middle" font-size="10.5" fill="#1d4ed8">{t}</text>')
# ---- 上段：畳み込み部（特徴抽出） ----
A('<rect x="16" y="46" width="728" height="150" rx="10" fill="#f8fafc" stroke="#e2e8f0"/>')
A('<text x="30" y="66" font-size="13" font-weight="bold" fill="#334155">特徴抽出（畳み込み ＋ プーリング）</text>')
y0=104
box(30,y0,84,64,"#f1f5f9","#64748b","#334155",[("入力",True),("1×28×28",False)])
arrow(118,y0+32,168,y0+32,["conv1","K=5, P=2","Cout=6"],y0-10,143)
box(172,y0,90,64,"#dbeafe","#2563eb","#1e3a8a",[("6×28×28",True),("+ReLU",False)])
arrow(266,y0+32,316,y0+32,["max pool","2×2, S=2"],y0-4,291)
box(320,y0+8,80,48,"#dbeafe","#2563eb","#1e3a8a",[("6×14×14",True)])
arrow(404,y0+32,454,y0+32,["conv2","K=5, P=0","Cout=16"],y0-10,429)
box(458,y0+8,80,48,"#dbeafe","#2563eb","#1e3a8a",[("16×10×10",True),("+ReLU",False)])
arrow(542,y0+32,592,y0+32,["max pool","2×2, S=2"],y0-4,567)
box(596,y0+14,72,36,"#dbeafe","#2563eb","#1e3a8a",[("16×5×5",True)])
# ---- 下段：全結合部（分類） ----
A('<rect x="16" y="210" width="728" height="100" rx="10" fill="#f8fafc" stroke="#e2e8f0"/>')
A('<text x="60" y="230" font-size="13" font-weight="bold" fill="#334155">分類（平坦化 ＋ 全結合）</text>')
y1=252
box(30,y1,110,44,"#ede9fe","#7c3aed","#4c1d95",[("平坦化 flatten",True),("16×5×5 = 400",False)])
arrow(144,y1+22,204,y1+22,["fc1","400→120"],y1-4,174)
box(208,y1,84,44,"#ffedd5","#c2410c","#7c2d12",[("120",True),("+ReLU",False)])
arrow(296,y1+22,356,y1+22,["fc2","120→84"],y1-4,326)
box(360,y1,84,44,"#ffedd5","#c2410c","#7c2d12",[("84",True),("+ReLU",False)])
arrow(448,y1+22,508,y1+22,["fc3","84→10"],y1-4,478)
box(512,y1,84,44,"#ffedd5","#c2410c","#7c2d12",[("出力 10",True),("各数字のスコア",False)],fs=11)
arrow(600,y1+22,650,y1+22,["argmax"],y1-4,625)
box(654,y1,82,44,"#dcfce7","#16a34a","#14532d",[("予測",True),("0〜9 のどれか",False)],fs=11)
# 上段末尾から下段先頭への折り返し
A(f'<path d="M 632 {y0+52} L 632 195 Q 632 203 624 203 L 50 203 Q 42 203 42 211 L 42 {y1-4}" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#ap)"/>')
A(f'<text x="340" y="190" text-anchor="middle" font-size="10.5" fill="#6d28d9">16×5×5 の特徴マップを1列（400個）に並べ直す</text>')
# 下部の注
A('<rect x="16" y="322" width="728" height="30" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>')
A('<text x="380" y="342" text-anchor="middle" font-size="11.5" fill="#1e3a8a">前半（青）で特徴を抽出し、後半（橙）で10クラスに分類する。各段の形は 公式 O = ⌊(W − K + 2P)/S⌋ + 1 で決まる。</text>')
A('</svg>')
import pathlib
OUT = pathlib.Path(__file__).resolve().parent / "svg" / "cnn_lenet.svg"   # gen/figs/svg/
OUT.write_text("\n".join(o))
