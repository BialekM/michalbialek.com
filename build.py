# Buduje stronę z src/page.html:
#   index.html      – wersja polska (https://michalbialek.com/)
#   en/index.html   – wersja angielska (https://michalbialek.com/en/)
#   sitemap.xml, robots.txt
# Teksty EN pochodzą ze słownika `const EN = {...}` w src/page.html, więc obie wersje są
# gotowym HTML-em (Google indeksuje je bez uruchamiania JavaScriptu).
import re, json, pathlib, os, datetime, html

ROOT = pathlib.Path(__file__).parent
SITE = "https://michalbialek.com"
src = (ROOT / "src" / "page.html").read_text(encoding="utf-8")
body = re.sub(r'^<title>.*?</title>\n<meta name="claude:viewport-fit-sides"[^>]*>\n', '', src, flags=re.S)

# Klucz formularza (sekret GitHub WEB3FORMS_KEY)
key = os.environ.get("WEB3FORMS_KEY", "").strip()
if key:
    body = body.replace('const WEB3FORMS_KEY = "";', 'const WEB3FORMS_KEY = "%s";' % key)

# Ścieżki bezwzględne, żeby działały też pod /en/
body = body.replace('src="assets/', 'src="/assets/').replace('href="assets/', 'href="/assets/')

a = src.index("const EN = {") + len("const EN = ")
EN = json.loads(src[a:src.index("\n};", a) + 2])

def translate(page, d):
    page = re.sub(r'(<(\w+)\b[^>]*\sdata-i18n="([^"]+)"[^>]*>)([^<]*)(</\2>)',
                  lambda m: m.group(1) + (html.escape(d[m.group(3)], quote=False) if m.group(3) in d else m.group(4)) + m.group(5), page)
    page = re.sub(r'(<(\w+)\b[^>]*\sdata-i18n-html="([^"]+)"[^>]*>)(.*?)(</\2>)',
                  lambda m: m.group(1) + (d.get(m.group(3), m.group(4))) + m.group(5), page, flags=re.S)
    page = re.sub(r'(<\w+\b[^>]*\sdata-i18n-ph="([^"]+)"[^>]*?\splaceholder=")([^"]*)(")',
                  lambda m: m.group(1) + html.escape(d.get(m.group(2), m.group(3))) + m.group(4), page)
    return page

def t_pl(k):
    m = re.search(r'data-i18n="%s">([^<]*)<' % re.escape(k), src)
    return html.unescape(m.group(1)) if m else k

SERVICES = ["s1", "s2", "s5", "s6", "s3", "s4", "s7", "s8", "s9"]
META = {
    "pl": dict(
        url=SITE + "/", locale="pl_PL", og="og-pl.png",
        title="Oprogramowanie na zamówienie i automatyzacja procesów – Wrocław | Michał Białek",
        desc="Aplikacje na zamówienie, automatyzacja procesów, integracje systemów i optymalizacja dla firm. Senior .NET i React developer z Wrocławia, 8+ lat doświadczenia. Bezpłatna konsultacja.",
        ogt="Michał Białek – oprogramowanie, które działa samo",
        svc=[t_pl(s + ".t") for s in SERVICES], catalog="Usługi"),
    "en": dict(
        url=SITE + "/en/", locale="en_GB", og="og-en.png",
        title="Custom Software Development & Process Automation – Wrocław, Poland | Michał Białek",
        desc="Custom applications, process automation, system integrations and performance optimisation for businesses. Senior .NET & React developer based in Wrocław, Poland, 8+ years of experience.",
        ogt="Michał Białek – software that runs itself",
        svc=[EN[s + ".t"] for s in SERVICES], catalog="Services"),
}

def jsonld(lang):
    m = META[lang]
    data = {"@context": "https://schema.org", "@graph": [
        {"@type": "ProfessionalService", "@id": SITE + "/#business",
         "name": "Michał Białek – Software", "url": m["url"], "description": m["desc"],
         "logo": SITE + "/assets/favicon-512.png", "image": SITE + "/assets/" + m["og"],
         "email": "contact@michalbialek.com", "telephone": "+48697340573",
         "address": {"@type": "PostalAddress", "streetAddress": "ul. Krzycka 86E", "postalCode": "53-020",
                     "addressLocality": "Wrocław", "addressRegion": "dolnośląskie", "addressCountry": "PL"},
         "areaServed": [{"@type": "City", "name": "Wrocław"}, {"@type": "Country", "name": "Polska"}, "Europe"],
         "knowsLanguage": ["pl", "en"], "founder": {"@id": SITE + "/#person"},
         "sameAs": ["https://www.linkedin.com/in/micha%C5%82-bia%C5%82ek-720b90141/", "https://github.com/BialekM"],
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": m["catalog"], "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in m["svc"]]}},
        {"@type": "Person", "@id": SITE + "/#person", "name": "Michał Białek", "jobTitle": "Senior Full Stack Developer",
         "url": SITE + "/", "email": "contact@michalbialek.com",
         "address": {"@type": "PostalAddress", "addressLocality": "Wrocław", "addressCountry": "PL"},
         "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Politechnika Wrocławska"},
                      {"@type": "CollegeOrUniversity", "name": "Uniwersytet Ekonomiczny we Wrocławiu"}],
         "knowsAbout": ["C#", ".NET", "ASP.NET Core", "React", "TypeScript", "SQL Server", "Entity Framework",
                        "Azure", "Microservices", "Domain-Driven Design", "Process automation", "System integration"],
         "sameAs": ["https://www.linkedin.com/in/micha%C5%82-bia%C5%82ek-720b90141/", "https://github.com/BialekM"]},
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Michał Białek",
         "inLanguage": ["pl-PL", "en"], "publisher": {"@id": SITE + "/#business"}},
    ]}
    return json.dumps(data, ensure_ascii=False, indent=1)

def head(lang):
    m = META[lang]; e = lambda s: html.escape(s, quote=True)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(m["title"])}</title>
<meta name="description" content="{e(m["desc"])}">
<meta name="author" content="Michał Białek">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0A1019">
<link rel="canonical" href="{m["url"]}">
<link rel="alternate" hreflang="pl" href="{SITE}/">
<link rel="alternate" hreflang="en" href="{SITE}/en/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Michał Białek">
<meta property="og:locale" content="{m["locale"]}">
<meta property="og:title" content="{e(m["ogt"])}">
<meta property="og:description" content="{e(m["desc"])}">
<meta property="og:url" content="{m["url"]}">
<meta property="og:image" content="{SITE}/assets/{m["og"]}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(m["ogt"])}">
<meta name="twitter:description" content="{e(m["desc"])}">
<meta name="twitter:image" content="{SITE}/assets/{m["og"]}">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/assets/favicon-180.png">
<script type="application/ld+json">
{jsonld(lang)}
</script>
<style>[hidden]{{display:none!important}}body{{margin:0}}:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}</style>
</head>
<body data-standalone="1">
'''

(ROOT / "index.html").write_text(head("pl") + body + "\n</body>\n</html>\n", encoding="utf-8")
(ROOT / "en").mkdir(exist_ok=True)
(ROOT / "en" / "index.html").write_text(head("en") + translate(body, EN) + "\n</body>\n</html>\n", encoding="utf-8")

today = datetime.date.today().isoformat()
alts = f'''    <xhtml:link rel="alternate" hreflang="pl" href="{SITE}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>'''
(ROOT / "sitemap.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{SITE}/</loc>
    <lastmod>{today}</lastmod>
{alts}
  </url>
  <url>
    <loc>{SITE}/en/</loc>
    <lastmod>{today}</lastmod>
{alts}
  </url>
</urlset>
''', encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
print("ok")
