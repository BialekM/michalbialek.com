# Składa samodzielny index.html z src/page.html (do hostingu, np. Netlify / Cloudflare Pages / GitHub Pages)
import re, pathlib, os
src = pathlib.Path(__file__).with_name("src").joinpath("page.html").read_text(encoding="utf-8")
body = re.sub(r'^<title>.*?</title>\n<meta name="claude:viewport-fit-sides"[^>]*>\n', '', src, flags=re.S)
head = '''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Michał Białek · Oprogramowanie na zamówienie, automatyzacja i optymalizacja dla firm</title>
<meta name="description" content="Aplikacje na zamówienie, automatyzacja procesów i optymalizacja systemów dla firm. Senior .NET i React developer z Wrocławia. Custom software, automation and optimisation for businesses.">
<meta property="og:title" content="Michał Białek · Oprogramowanie dla firm">
<meta property="og:description" content="Zamieniam ręczną robotę w Twojej firmie w oprogramowanie, które działa samo.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://michalbialek.com/">
<link rel="canonical" href="https://michalbialek.com/">
<link rel="icon" type="image/svg+xml" href="assets/ikona-laptop-MB-jasne-tlo.svg">
<link rel="apple-touch-icon" href="assets/ikona-laptop-MB-jasne-tlo-180.png">
<link rel="alternate" hreflang="pl" href="?lang=pl">
<link rel="alternate" hreflang="en" href="?lang=en">
<style>[hidden]{display:none!important}body{margin:0}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
</head>
<body data-standalone="1">
'''
key = os.environ.get("WEB3FORMS_KEY", "").strip()
if key:
    body = body.replace('const WEB3FORMS_KEY = "";', 'const WEB3FORMS_KEY = "%s";' % key)
pathlib.Path(__file__).with_name("index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
print("ok")
