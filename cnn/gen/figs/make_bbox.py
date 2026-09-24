o=[]; A=o.append
W,H=760,380
def S(base,sub): return f'{base}<tspan baseline-shift="sub" font-size="8.5">{sub}</tspan>'
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Noto Sans CJK JP, sans-serif">')
A('<defs><marker id="ab" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#2563eb"/></marker></defs>')
A('<text x="380" y="26" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e3a8a">ネットワークが出す (x, y, w, h) は相対値：枠に戻すには変換が要る</text>')
# ---- left ----
gx,gy,cs=30,72,52
A(f'<text x="{gx+2*cs}" y="56" text-anchor="middle" font-size="12" fill="#334155">特徴マップのグリッド（13×13 の一部）</text>')
A(f'<rect x="{gx+cs}" y="{gy+cs}" width="{cs}" height="{cs}" fill="#dbeafe"/>')
for i in range(5):
    A(f'<line x1="{gx+i*cs}" y1="{gy}" x2="{gx+i*cs}" y2="{gy+4*cs}" stroke="#94a3b8" stroke-width="1.5"/>')
    A(f'<line x1="{gx}" y1="{gy+i*cs}" x2="{gx+4*cs}" y2="{gy+i*cs}" stroke="#94a3b8" stroke-width="1.5"/>')
cx0,cy0=gx+cs,gy+cs
A(f'<circle cx="{cx0}" cy="{cy0}" r="3.5" fill="#1e3a8a"/>')
A(f'<text x="{cx0+4}" y="{cy0-7}" text-anchor="start" font-size="11" fill="#1e3a8a">担当セルの左上 ({S("g","i")}, {S("g","j")})</text>')
bx,by=cx0+0.65*cs,cy0+0.6*cs
A(f'<line x1="{cx0}" y1="{by}" x2="{bx}" y2="{by}" stroke="#2563eb" stroke-width="2" marker-end="url(#ab)"/>')
A(f'<line x1="{bx}" y1="{cy0}" x2="{bx}" y2="{by}" stroke="#2563eb" stroke-width="2" marker-end="url(#ab)"/>')
A(f'<circle cx="{bx}" cy="{by}" r="4" fill="#2563eb"/>')
A(f'<text x="{cx0+0.3*cs}" y="{by+13}" text-anchor="middle" font-size="10.5" fill="#1d4ed8">σ({S("t","x")})</text>')
A(f'<text x="{bx+15}" y="{cy0+0.32*cs+3}" text-anchor="middle" font-size="10.5" fill="#1d4ed8">σ({S("t","y")})</text>')
aw,ah=1.7*cs,1.3*cs
A(f'<rect x="{bx-aw/2}" y="{by-ah/2}" width="{aw}" height="{ah}" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4"/>')
bw,bh=aw*1.3,ah*0.75
A(f'<rect x="{bx-bw/2}" y="{by-bh/2}" width="{bw}" height="{bh}" fill="none" stroke="#dc2626" stroke-width="2.5"/>')
# legend under grid
ly=gy+4*cs+18
A(f'<circle cx="{gx+6}" cy="{ly-4}" r="4" fill="#2563eb"/><text x="{gx+16}" y="{ly}" font-size="11" fill="#1d4ed8">枠の中心 ({S("b","x")}, {S("b","y")})</text>')
A(f'<line x1="{gx+150}" y1="{ly-4}" x2="{gx+176}" y2="{ly-4}" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4"/><text x="{gx+182}" y="{ly}" font-size="11" fill="#92400e">アンカー ({S("a","w")}, {S("a","h")})：基準の枠</text>')
ly+=18
A(f'<line x1="{gx+150}" y1="{ly-4}" x2="{gx+176}" y2="{ly-4}" stroke="#dc2626" stroke-width="2.5"/><text x="{gx+182}" y="{ly}" font-size="11" fill="#b91c1c">予測枠 ({S("b","w")}, {S("b","h")})</text>')
# ---- right ----
rx=400
A(f'<rect x="{rx-14}" y="48" width="{W-rx}" height="{gy+4*cs-48+56}" rx="10" fill="#f8fafc" stroke="#e2e8f0"/>')
A(f'<text x="{rx}" y="72" font-size="13" font-weight="bold" fill="#334155">ネットワークの生の出力 {S("t","x")}, {S("t","y")}, {S("t","w")}, {S("t","h")} を枠に戻す式</text>')
y=100
A(f'<text x="{rx}" y="{y}" font-size="12" font-weight="bold" fill="#1d4ed8">位置</text>')
A(f'<text x="{rx+48}" y="{y}" font-size="12.5" fill="#1d4ed8">{S("b","x")} = {S("g","i")} + σ({S("t","x")})　　{S("b","y")} = {S("g","j")} + σ({S("t","y")})</text>'); y+=20
A(f'<text x="{rx+48}" y="{y}" font-size="11.5" fill="#1d4ed8">担当セルの左上からの「ずれ」（0〜1、セル1個 = 1）</text>'); y+=32
A(f'<text x="{rx}" y="{y}" font-size="12" font-weight="bold" fill="#b91c1c">大きさ</text>')
A(f'<text x="{rx+48}" y="{y}" font-size="12.5" fill="#b91c1c">{S("b","w")} = {S("a","w")} · e<tspan baseline-shift="super" font-size="9">{S("t","w")}</tspan>　　{S("b","h")} = {S("a","h")} · e<tspan baseline-shift="super" font-size="9">{S("t","h")}</tspan></text>'); y+=20
A(f'<text x="{rx+48}" y="{y}" font-size="11.5" fill="#b91c1c">アンカー枠（ピクセル単位）に対する「倍率」</text>'); y+=32
A(f'<text x="{rx}" y="{y}" font-size="12" font-weight="bold" fill="#334155">画像座標</text>')
A(f'<text x="{rx+64}" y="{y}" font-size="12" fill="#334155">{S("b","x")}, {S("b","y")} × 1セルの大きさ（416 ÷ 13 = 32 画素）</text>'); y+=18
A(f'<text x="{rx+64}" y="{y}" font-size="11.5" fill="#334155">{S("b","w")}, {S("b","h")} はそのまま（アンカーが画素単位のため）</text>'); y+=26
A(f'<text x="{rx}" y="{y}" font-size="11" fill="#64748b">σ はシグモイド関数（値を 0〜1 に押し込める）</text>')
# bottom note
A('<rect x="16" y="326" width="728" height="46" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>')
A('<text x="380" y="345" text-anchor="middle" font-size="12" fill="#1e3a8a">出力テンソルの x, y は担当セルから見た相対位置、w, h はアンカー枠から見た相対的な大きさ。</text>')
A('<text x="380" y="363" text-anchor="middle" font-size="12" fill="#1e3a8a">画像上のピクセル座標そのものではなく、後処理でこの変換をしてから NMS にかける（本番の C++ コードが行う）。</text>')
A('</svg>')
import pathlib
OUT = pathlib.Path(__file__).resolve().parent / "svg" / "cnn_bbox.svg"   # gen/figs/svg/
OUT.write_text("\n".join(o))
