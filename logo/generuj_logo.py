# Generator logo (SVG, tekst zamieniony na krzywe). Wymaga: pip install fonttools; czcionki w katalogu FONTS.
import sys, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTS = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
F = {k: TTFont(FONTS / f) for k, f in {"mono": "jbm500.ttf", "monob": "jbm700.ttf", "disp": "sg900.ttf"}.items()}

def text(s, font, size, x, y, fill, anchor="start", spacing=0.0):
    f = F[font]; gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm; hm = f["hmtx"]
    sc = size / upm; names = [cmap.get(ord(c), ".notdef") for c in s]
    width = sum(hm[n][0] for n in names) * sc + spacing * (len(s) - 1)
    cx = x - (width if anchor == "end" else width / 2 if anchor == "middle" else 0)
    out = []
    for n in names:
        pen = SVGPathPen(gs)
        gs[n].draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
        d = pen.getCommands()
        if d: out.append(d)
        cx += hm[n][0] * sc + spacing
    return f'<path fill="{fill}" d="{" ".join(out)}"/>', width

SYN = {"kw": "#C586C0", "fn": "#DCDCAA", "var": "#9CDCFE", "p": "#D4D4D4", "cm": "#6A9955", "ln": "#6E7681"}
SLOGANS = {
    "A": [[("cm", "// less clicking, more doing")], [("kw", "if"), ("p", " ("), ("var", "manual"), ("p", ") {")], [("p", "  "), ("fn", "automate"), ("p", "();")], [("p", "}")]],
    "B": [[("cm", "// from idea to production")], [("kw", "while"), ("p", " ("), ("var", "ideas"), ("p", ") {")], [("p", "  "), ("fn", "build"), ("p", "();")], [("p", "}")]],
    "C": [[("cm", "// make it fast")], [("kw", "if"), ("p", " ("), ("var", "slow"), ("p", ") {")], [("p", "  "), ("fn", "optimize"), ("p", "();")], [("p", "}")]],
}
THEMES = {
    "jasne": dict(lid="#151C2A", deck="#202938", lip="#0E141F", hinge="#0A0F18", key="#353F52", keyedge="#1A212E", pad="#2A3344"),
    "ciemne": dict(lid="#C7CFDB", deck="#DCE2EA", lip="#9AA5B6", hinge="#8A95A6", key="#F4F6F9", keyedge="#AEB8C6", pad="#CBD3DE"),
}
ACC, ACC2 = "#2A43DB", "#4F66FF"

def laptop(slogan, th):
    t = THEMES[th]; o = []
    u = f"{slogan}{th}"
    o.append(f'<defs><filter id="g{u}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3.2"/></filter>'
             f'<linearGradient id="k{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ACC2}"/><stop offset="1" stop-color="{ACC}"/></linearGradient></defs>')
    # pokrywa i ekran
    o.append(f'<rect x="28" y="6" width="200" height="132" rx="10" fill="{t["lid"]}"/>')
    o.append('<rect x="35" y="13" width="186" height="117" rx="3" fill="#1E1E1E"/>')
    o.append('<path d="M38 13h180a3 3 0 0 1 3 3v7H35v-7a3 3 0 0 1 3-3z" fill="#2D2D30"/>')
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]): o.append(f'<circle cx="{42+i*6}" cy="18" r="1.8" fill="{c}"/>')
    o.append('<rect x="35" y="23" width="11" height="107" fill="#333337"/>')
    o.append(f'<rect x="35" y="27" width="1.4" height="8" fill="{ACC2}"/>')
    for i in range(3): o.append(f'<rect x="38" y="{28+i*11}" width="5.5" height="5.5" rx="1.2" fill="{"#C5C5C5" if i==0 else "#6E6E73"}"/>')
    o.append('<rect x="46" y="23" width="175" height="9" fill="#252526"/>')
    o.append('<rect x="46" y="23" width="40" height="9" fill="#1E1E1E"/>')
    o.append(f'<rect x="46" y="23" width="40" height="1" fill="{ACC2}"/>')
    p, _ = text("mb.ts", "mono", 5.2, 52, 29.6, "#D4D4D4"); o.append(p)
    o.append('<rect x="46" y="124" width="175" height="6" fill="#007ACC"/>')
    p, _ = text("main", "mono", 4, 50, 128.6, "#FFFFFF"); o.append(p)
    lh, y0, size = 21, 52, 10.8
    for li, toks in enumerate(SLOGANS[slogan]):
        y = y0 + li * lh
        p, _ = text(str(li + 1), "mono", 7, 57, y, SYN["ln"], "end"); o.append(p)
        x = 63
        for kind, s in toks:
            p, w = text(s, "mono" if kind == "cm" else "monob", size if kind != "cm" else 8.2, x, y, SYN[kind]); o.append(p); x += w
        if li == 2: o.append(f'<rect x="{x+1.5}" y="{y-8.5}" width="1.6" height="10.5" fill="#AEAFAD"/>')
    # zawias i spód
    o.append(f'<rect x="22" y="138" width="212" height="4" rx="1" fill="{t["hinge"]}"/>')
    o.append(f'<path d="M22 142H234L252 188H4Z" fill="{t["deck"]}"/>')
    o.append(f'<path d="M4 188H252v3a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z" fill="{t["lip"]}"/>')
    def P(u, v):
        y = 142 + 46 * v; xl = 22 - 18 * v; xr = 234 + 18 * v; return xl + (xr - xl) * u, y
    def quad(u0, u1, v0, v1):
        pts = [P(u0, v0), P(u1, v0), P(u1, v1), P(u0, v1)]; return "M" + "L".join(f"{a:.2f} {b:.2f}" for a, b in pts) + "Z"
    U0, U1, N = 0.07, 0.93, 11.0; cu = lambda c: U0 + (U1 - U0) * c / N
    rows = [(0.08, 0.22), (0.25, 0.39), (0.42, 0.56), (0.59, 0.70)]
    G = 0.1; keys = []
    keys += [(c, c + 1 - G, 0, None) for c in range(11)]
    keys += [(0.35 + c, 1.35 + c - G, 1, None) for c in range(10)]
    keys += [(0, 1.6 - G, 2, None)] + [(1.7 + i, 2.7 + i - G, 2, ch) for i, ch in enumerate("ZXCVBNM")] + [(8.7, 11, 2, None)]
    keys += [(0, 1.1 - G, 3, None), (1.2, 2.3 - G, 3, None), (2.4, 8.6 - G, 3, None), (8.7, 9.8 - G, 3, None), (9.9, 11, 3, None)]
    hl = []
    for c0, c1, r, ch in keys:
        v0, v1 = rows[r]; on = ch in ("M", "B")
        if on: hl.append((c0, c1, v0, v1, ch)); continue
        o.append(f'<path d="{quad(cu(c0), cu(c1), v0, v1)}" fill="{t["key"]}"/>')
    o.append(f'<path d="{quad(0.38, 0.62, 0.76, 0.95)}" fill="{t["pad"]}"/>')
    for c0, c1, v0, v1, ch in hl:
        o.append(f'<path d="{quad(cu(c0)-.01, cu(c1)+.01, v0-.03, v1+.04)}" fill="{ACC2}" opacity=".85" filter="url(#g{u})"/>')
        o.append(f'<path d="{quad(cu(c0), cu(c1), v0+.02, v1+.02)}" fill="#1B2C8F"/>')
        o.append(f'<path d="{quad(cu(c0), cu(c1), v0-.015, v1-.015)}" fill="url(#k{u})"/>')
        cx, cy = P((cu(c0) + cu(c1)) / 2, (v0 + v1) / 2)
        p, _ = text(ch, "disp", 8.5, cx, cy + 3.1, "#FFFFFF", "middle"); o.append(p)
    return "\n".join(o)

def svg(vb, body, w=None, h=None):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{f" width={chr(34)}{w}{chr(34)} height={chr(34)}{h}{chr(34)}" if w else ""}>\n{body}\n</svg>\n'

def keys_icon(dark_bg=False):
    o = ['<defs><linearGradient id="kk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % (ACC2, ACC)]
    for i, ch in enumerate("MB"):
        x = 4 + i * 29
        o.append(f'<rect x="{x}" y="14" width="27" height="38" rx="6" fill="#1B2C8F"/>')
        o.append(f'<rect x="{x}" y="10" width="27" height="38" rx="6" fill="url(#kk)"/>')
        o.append(f'<rect x="{x+3}" y="12.5" width="21" height="28" rx="4" fill="#FFFFFF" opacity=".10"/>')
        p, _ = text(ch, "disp", 20, x + 13.5, 36.5, "#FFFFFF", "middle"); o.append(p)
    return "\n".join(o)

for s in SLOGANS:
    for th in THEMES:
        (OUT / f"logo-laptop-{s}-{th}-tlo.svg").write_text(svg("0 0 256 200", laptop(s, th)), encoding="utf-8")
# poziomy: ikona + nazwa
for th, ink, sub in [("jasne", "#0D1726", "#566275"), ("ciemne", "#F2F5F9", "#9AA6B8")]:
    for s in SLOGANS:
        n, nw = text("Michał Białek", "disp", 54, 280, 104, ink)
        t2, tw = text("SOFTWARE · AUTOMATION", "mono", 17, 283, 140, sub, spacing=3.2)
        W = int(280 + max(nw, tw) + 12)
        (OUT / f"logo-poziome-{s}-{th}-tlo.svg").write_text(svg(f"0 0 {W} 200", laptop(s, th) + "\n" + n + "\n" + t2), encoding="utf-8")
(OUT / "ikona-MB.svg").write_text(svg("0 0 64 64", keys_icon()), encoding="utf-8")

def laptop_icon(th):
    lid, base, lip = ("#151C2A", "#232C3E", "#0E141F") if th == "jasne" else ("#C7CFDB", "#DCE2EA", "#9AA5B6")
    u = "li" + th
    o = [f'<defs><linearGradient id="{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ACC2}"/><stop offset="1" stop-color="{ACC}"/></linearGradient>'
         f'<filter id="{u}g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2"/></filter></defs>']
    o.append(f'<rect x="7" y="9" width="50" height="36" rx="4" fill="{lid}"/>')
    o.append('<rect x="10" y="12" width="44" height="30" rx="1.5" fill="#0D1220"/>')
    o.append(f'<rect x="14" y="17" width="36" height="20" rx="4" fill="{ACC}" opacity=".45" filter="url(#{u}g)"/>')
    for i, ch in enumerate("MB"):
        x = 14.5 + i * 18
        o.append(f'<rect x="{x}" y="18.5" width="17" height="20" rx="3.2" fill="#1B2C8F"/>')
        o.append(f'<rect x="{x}" y="16" width="17" height="20" rx="3.2" fill="url(#{u})"/>')
        o.append(f'<rect x="{x+2}" y="17.5" width="13" height="14" rx="2.2" fill="#FFFFFF" opacity=".10"/>')
        pth, _ = text(ch, "disp", 13, x + 8.5, 31, "#FFFFFF", "middle"); o.append(pth)
    o.append(f'<path d="M5 45H59L63 51.5a2 2 0 0 1-1.8 2.5H2.8A2 2 0 0 1 1 51.5Z" fill="{base}"/>')
    o.append(f'<rect x="25" y="45" width="14" height="2.4" rx="1.2" fill="{lip}"/>')
    return "\n".join(o)
for th in ("jasne", "ciemne"):
    (OUT / f"ikona-laptop-MB-{th}-tlo.svg").write_text(svg("0 0 64 64", laptop_icon(th)), encoding="utf-8")
print("ok")
