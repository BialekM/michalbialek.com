# Favicon: litery MB wypełniające całą ikonę. Użycie: python3 favicon.py KATALOG_CZCIONEK KATALOG_WYJSCIA
import sys, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
f = TTFont(pathlib.Path(sys.argv[1]) / "sg900.ttf"); out = pathlib.Path(sys.argv[2])
gs = f.getGlyphSet(); cmap = f.getBestCmap(); hm = f["hmtx"]
names = [cmap[ord(c)] for c in "MB"]
# rzeczywiste granice liter
x = 0; minx = miny = 1e9; maxx = maxy = -1e9; offs = []
for n in names:
    bp = BoundsPen(gs); gs[n].draw(bp); b = bp.bounds
    minx = min(minx, x + b[0]); maxx = max(maxx, x + b[2]); miny = min(miny, b[1]); maxy = max(maxy, b[3])
    offs.append(x); x += hm[n][0] - 30
W, H = maxx - minx, maxy - miny
sc = min(50 / W, 34 / H)  # litery zajmują ok. 50 z 64 px szerokości
tx = 32 - (minx + W / 2) * sc; ty = 32 + (miny + H / 2) * sc
d = []
for n, o in zip(names, offs):
    pen = SVGPathPen(gs); gs[n].draw(TransformPen(pen, (sc, 0, 0, -sc, tx + o * sc, ty))); d.append(pen.getCommands())
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="fg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4F66FF"/><stop offset="1" stop-color="#1F35C4"/></linearGradient></defs>
<rect width="64" height="64" rx="14" fill="url(#fg)"/>
<path fill="#FFFFFF" d="{' '.join(d)}"/>
</svg>
'''
(out / "favicon.svg").write_text(svg, encoding="utf-8"); print("ok")
