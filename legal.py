# Polityka prywatności i regulamin (PL + EN). Wywoływane z build.py.
#
# >>> DO UZUPEŁNIENIA, gdy założysz działalność gospodarczą <<<
# Wpisz pełną nazwę firmy z CEIDG i NIP (REGON opcjonalnie). Puste pola nie pojawiają się na stronie.
COMPANY = {
    "name": "",    # np. "Michał Białek Software" (pełna nazwa z CEIDG)
    "nip": "",     # np. "8990000000"
    "regon": "",
}
OWNER = "Michał Białek"
ADDRESS_PL = "ul. Krzycka 86E, 53-020 Wrocław"
ADDRESS_EN = "ul. Krzycka 86E, 53-020 Wrocław, Poland"
EMAIL = "contact@michalbialek.com"
UPDATED = "13.11.2026"
UPDATED_EN = "13 November 2026"

SITE = "https://michalbialek.com"

def _who(lang):
    name = COMPANY["name"].strip()
    if lang == "pl":
        s = f"{OWNER}" + (f", prowadzący działalność gospodarczą pod firmą <b>{name}</b>" if name else "")
        s += f", {ADDRESS_PL}"
        if COMPANY["nip"].strip(): s += f", NIP {COMPANY['nip'].strip()}"
        if COMPANY["regon"].strip(): s += f", REGON {COMPANY['regon'].strip()}"
    else:
        s = f"{OWNER}" + (f", trading as <b>{name}</b>" if name else "")
        s += f", {ADDRESS_EN}"
        if COMPANY["nip"].strip(): s += f", tax ID (NIP) {COMPANY['nip'].strip()}"
        if COMPANY["regon"].strip(): s += f", REGON {COMPANY['regon'].strip()}"
    return s

MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

def privacy_pl():
    return f"""
<h1>Polityka prywatności</h1>
<p class="upd">Obowiązuje od {UPDATED}</p>
<p>Ta strona wyjaśnia, jakie dane zbieram w serwisie michalbialek.com, po co i jak długo je przechowuję oraz jakie masz prawa. Piszę prosto, bez prawniczego żargonu.</p>

<h2>1. Administrator danych</h2>
<p>Administratorem Twoich danych osobowych jest {_who("pl")} (dalej: „ja”). We wszystkich sprawach dotyczących danych możesz pisać na {MAIL}.</p>

<h2>2. Jakie dane i w jakim celu</h2>
<h3>Formularz kontaktowy i e-mail</h3>
<p>Gdy wysyłasz formularz albo piszesz do mnie bezpośrednio, przetwarzam: imię i nazwisko, adres e-mail, opcjonalnie nazwę firmy i numer telefonu, treść wiadomości oraz wybrane tematy. Używam ich, żeby odpowiedzieć na zapytanie, przygotować ofertę i prowadzić dalszą rozmowę.</p>
<ul>
<li>Podstawa prawna: art. 6 ust. 1 lit. b RODO (działania przed zawarciem umowy na Twoje żądanie), art. 6 ust. 1 lit. f RODO (mój prawnie uzasadniony interes, czyli odpowiedź na korespondencję) oraz Twoja zgoda wyrażona w formularzu (art. 6 ust. 1 lit. a RODO).</li>
<li>Podanie danych jest dobrowolne, ale bez adresu e-mail i opisu sprawy nie mogę odpowiedzieć.</li>
</ul>
<h3>Współpraca</h3>
<p>Jeśli podpiszemy umowę, dane potrzebne do jej wykonania i rozliczenia przetwarzam na podstawie art. 6 ust. 1 lit. b RODO, a dane wymagane przez przepisy podatkowe i rachunkowe na podstawie art. 6 ust. 1 lit. c RODO.</p>
<h3>Logi serwera</h3>
<p>Serwer, na którym działa strona, automatycznie zapisuje techniczne informacje o wizytach (adres IP, data i godzina, adres podstrony, typ przeglądarki). Służą one bezpieczeństwu i diagnozowaniu błędów (art. 6 ust. 1 lit. f RODO). Nie łączę ich z innymi danymi i nie używam do śledzenia odwiedzających.</p>

<h2>3. Komu przekazuję dane</h2>
<ul>
<li><b>OVH sp. z o.o.</b> (grupa OVHcloud) – hosting strony i skrzynki e-mail, serwery w Unii Europejskiej.</li>
<li><b>Web3Forms</b> – usługa, która przekazuje treść formularza na moją skrzynkę e-mail. Dostawca może przetwarzać dane poza Europejskim Obszarem Gospodarczym. W takim przypadku przekazanie odbywa się na podstawie mechanizmów przewidzianych w RODO, np. standardowych klauzul umownych zatwierdzonych przez Komisję Europejską.</li>
<li><b>Google</b> – tylko jeśli klikniesz „Pokaż mapę Google” w sekcji kontakt. Dopiero wtedy przeglądarka łączy się z Google Maps, a Google przetwarza dane zgodnie z własną polityką prywatności (policies.google.com/privacy).</li>
<li>Moja księgowość i organy publiczne – tylko gdy dojdzie do współpracy albo wymagają tego przepisy.</li>
</ul>
<p>Nie sprzedaję danych i nie przekazuję ich w celach marketingowych.</p>

<h2>4. Jak długo przechowuję dane</h2>
<ul>
<li>Korespondencja z zapytaniem, które nie zakończyło się współpracą: do 12 miesięcy od ostatniej wiadomości, chyba że wcześniej poprosisz o usunięcie.</li>
<li>Dane związane z umową: przez czas współpracy i do upływu okresu przedawnienia roszczeń, a dokumenty rozliczeniowe przez okres wymagany przepisami podatkowymi (zwykle 5 lat od końca roku podatkowego).</li>
<li>Logi serwera: zgodnie z ustawieniami hostingu, zwykle kilka tygodni.</li>
</ul>

<h2>5. Twoje prawa</h2>
<p>Masz prawo do dostępu do swoich danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przeniesienia oraz do sprzeciwu wobec przetwarzania opartego na prawnie uzasadnionym interesie. Zgodę możesz wycofać w dowolnym momencie, co nie wpływa na zgodność z prawem przetwarzania przed jej wycofaniem. Wystarczy e-mail na {MAIL}.</p>
<p>Masz też prawo wnieść skargę do Prezesa Urzędu Ochrony Danych Osobowych (ul. Stawki 2, 00-193 Warszawa, uodo.gov.pl).</p>
<p>Nie podejmuję wobec Ciebie decyzji w sposób zautomatyzowany i nie profiluję Cię.</p>

<h2>6. Pliki cookies i pamięć przeglądarki</h2>
<p>Strona nie używa plików cookies ani narzędzi analitycznych i reklamowych. Czcionki są ładowane z mojego serwera, a nie z zewnętrznych usług. W pamięci przeglądarki (localStorage) zapisuję jedynie wybraną wersję językową, żeby przy następnej wizycie wyświetlić ją ponownie. Możesz ją usunąć w ustawieniach przeglądarki.</p>

<h2>7. Zmiany</h2>
<p>Jeśli zmienię sposób przetwarzania danych, zaktualizuję tę stronę i datę na górze.</p>
"""

def privacy_en():
    return f"""
<h1>Privacy policy</h1>
<p class="upd">Effective from {UPDATED_EN}</p>
<p>This page explains what data I collect on michalbialek.com, why, how long I keep it and what rights you have. I keep it plain and simple.</p>

<h2>1. Data controller</h2>
<p>The controller of your personal data is {_who("en")} ("I", "me"). For anything related to your data, write to {MAIL}.</p>

<h2>2. What data and why</h2>
<h3>Contact form and e-mail</h3>
<p>When you send the form or e-mail me directly, I process your name, e-mail address, optionally your company name and phone number, the message and the topics you selected. I use them to reply to your enquiry, prepare a proposal and continue the conversation.</p>
<ul>
<li>Legal basis: Art. 6(1)(b) GDPR (steps taken at your request before entering into a contract), Art. 6(1)(f) GDPR (my legitimate interest in answering correspondence) and the consent you give in the form (Art. 6(1)(a) GDPR).</li>
<li>Providing the data is voluntary, but I cannot reply without an e-mail address and a short description.</li>
</ul>
<h3>Working together</h3>
<p>If we sign a contract, I process the data needed to perform and invoice it under Art. 6(1)(b) GDPR, and data required by tax and accounting law under Art. 6(1)(c) GDPR.</p>
<h3>Server logs</h3>
<p>The web server automatically records technical information about visits (IP address, date and time, page address, browser type). It is used for security and troubleshooting (Art. 6(1)(f) GDPR). I do not combine it with other data or use it to track visitors.</p>

<h2>3. Who receives the data</h2>
<ul>
<li><b>OVH sp. z o.o.</b> (OVHcloud group) – website and e-mail hosting, servers in the European Union.</li>
<li><b>Web3Forms</b> – a service that delivers the form message to my mailbox. The provider may process data outside the European Economic Area. In that case the transfer relies on safeguards provided for in the GDPR, such as the European Commission's standard contractual clauses.</li>
<li><b>Google</b> – only if you click "Show Google map" in the contact section. Only then does your browser connect to Google Maps, and Google processes data under its own privacy policy (policies.google.com/privacy).</li>
<li>My accountant and public authorities – only if we work together or the law requires it.</li>
</ul>
<p>I do not sell data or share it for marketing purposes.</p>

<h2>4. How long I keep data</h2>
<ul>
<li>Enquiries that did not lead to a project: up to 12 months after the last message, unless you ask me to delete them sooner.</li>
<li>Contract data: for the duration of the work and until any claims become time-barred; accounting records for the period required by tax law (usually 5 years from the end of the tax year).</li>
<li>Server logs: according to the hosting settings, usually a few weeks.</li>
</ul>

<h2>5. Your rights</h2>
<p>You have the right to access, rectify and erase your data, to restrict processing, to data portability and to object to processing based on legitimate interest. You can withdraw your consent at any time, which does not affect processing carried out before the withdrawal. Just e-mail {MAIL}.</p>
<p>You also have the right to lodge a complaint with the Polish supervisory authority, the President of the Personal Data Protection Office (ul. Stawki 2, 00-193 Warszawa, uodo.gov.pl), or with the authority in your country.</p>
<p>I do not make automated decisions about you or profile you.</p>

<h2>6. Cookies and browser storage</h2>
<p>This website does not use cookies, analytics or advertising tools. Fonts are served from my own server, not from third-party services. The only thing stored in your browser (localStorage) is your chosen language, so it is shown again on your next visit. You can clear it in your browser settings.</p>

<h2>7. Changes</h2>
<p>If I change how data is processed, I will update this page and the date at the top.</p>
"""

def terms_pl():
    return f"""
<h1>Regulamin serwisu</h1>
<p class="upd">Obowiązuje od {UPDATED}</p>

<h2>1. Postanowienia ogólne</h2>
<p>Regulamin określa zasady korzystania z serwisu michalbialek.com, w tym z formularza kontaktowego. Jest to regulamin świadczenia usług drogą elektroniczną w rozumieniu ustawy z dnia 18 lipca 2002 r. o świadczeniu usług drogą elektroniczną.</p>
<p>Usługodawcą jest {_who("pl")}, e-mail {MAIL}.</p>

<h2>2. Usługi w serwisie</h2>
<ul>
<li>przeglądanie informacji o moich usługach,</li>
<li>wysłanie zapytania przez formularz kontaktowy.</li>
</ul>
<p>Korzystanie z serwisu jest bezpłatne i nie wymaga zakładania konta. Umowa o korzystanie z formularza zostaje zawarta z chwilą jego wysłania i wygasa po udzieleniu odpowiedzi. Z przeglądania strony możesz zrezygnować w każdej chwili, opuszczając ją.</p>

<h2>3. Wymagania techniczne</h2>
<p>Wystarczy urządzenie z dostępem do internetu, aktualna przeglądarka z włączonym JavaScriptem oraz aktywny adres e-mail, jeśli chcesz otrzymać odpowiedź.</p>

<h2>4. Zasady korzystania</h2>
<p>Zabronione jest przesyłanie przez formularz treści bezprawnych, obraźliwych, spamu oraz oprogramowania mogącego zakłócić działanie serwisu. Podawaj dane prawdziwe i własne.</p>

<h2>5. Charakter informacji</h2>
<p>Informacje w serwisie, w tym opisy usług, nie stanowią oferty w rozumieniu art. 66 Kodeksu cywilnego, tylko zaproszenie do rozmowy. Zakres, termin i cenę każdej współpracy ustalamy indywidualnie w osobnej umowie. Na życzenie klienta zapewniam pełną poufność, także w formie umowy NDA.</p>

<h2>6. Reklamacje</h2>
<p>Uwagi i reklamacje dotyczące działania serwisu możesz zgłaszać na {MAIL}. Odpowiadam w ciągu 14 dni od otrzymania zgłoszenia.</p>

<h2>7. Prawa autorskie</h2>
<p>Treści, grafiki, logo i kod serwisu są chronione prawem autorskim. Kopiowanie ich w całości lub części wymaga mojej zgody.</p>

<h2>8. Dane osobowe</h2>
<p>Zasady przetwarzania danych opisuje <a href="/polityka-prywatnosci/">polityka prywatności</a>.</p>

<h2>9. Postanowienia końcowe</h2>
<p>Regulamin podlega prawu polskiemu. Mogę go zmienić z ważnych przyczyn, np. zmiany przepisów lub funkcji serwisu. Zmiany nie wpływają na zapytania wysłane wcześniej. Konsument może skorzystać z pozasądowych sposobów rozwiązywania sporów, m.in. przez miejskiego rzecznika konsumentów.</p>
"""

def terms_en():
    return f"""
<h1>Website terms</h1>
<p class="upd">Effective from {UPDATED_EN}</p>

<h2>1. General</h2>
<p>These terms set out the rules for using michalbialek.com, including the contact form. They are terms of electronic services under the Polish Act of 18 July 2002 on the provision of electronic services.</p>
<p>The service provider is {_who("en")}, e-mail {MAIL}.</p>

<h2>2. Services on the website</h2>
<ul>
<li>browsing information about my services,</li>
<li>sending an enquiry through the contact form.</li>
</ul>
<p>Using the website is free and requires no account. The agreement to use the form is concluded when you send it and ends once I have replied. You can stop browsing at any time by leaving the website.</p>

<h2>3. Technical requirements</h2>
<p>A device with internet access, an up-to-date browser with JavaScript enabled and, if you want a reply, a working e-mail address.</p>

<h2>4. Rules of use</h2>
<p>Do not send unlawful or offensive content, spam or software that could disrupt the website through the form. Please provide accurate data that belongs to you.</p>

<h2>5. Nature of the information</h2>
<p>Information on the website, including service descriptions, is not an offer within the meaning of Art. 66 of the Polish Civil Code but an invitation to talk. The scope, timeline and price of every project are agreed individually in a separate contract. On request I guarantee full confidentiality, including under an NDA.</p>

<h2>6. Complaints</h2>
<p>Send comments or complaints about the website to {MAIL}. I reply within 14 days of receiving them.</p>

<h2>7. Copyright</h2>
<p>The texts, graphics, logo and code of this website are protected by copyright. Copying them in whole or in part requires my permission.</p>

<h2>8. Personal data</h2>
<p>How I process personal data is described in the <a href="/en/privacy-policy/">privacy policy</a>.</p>

<h2>9. Final provisions</h2>
<p>These terms are governed by Polish law. I may change them for valid reasons, such as changes in the law or in the website's features. Changes do not affect enquiries sent earlier. Consumers may use out-of-court dispute resolution, for example through a local consumer ombudsman.</p>
"""

PAGES = [
    # (ścieżka, język, tytuł, opis, treść, ścieżka odpowiednika w drugim języku)
    ("polityka-prywatnosci/", "pl", "Polityka prywatności | Michał Białek", "Jakie dane zbiera serwis michalbialek.com, w jakim celu i jakie masz prawa (RODO).", privacy_pl, "en/privacy-policy/"),
    ("en/privacy-policy/", "en", "Privacy policy | Michał Białek", "What data michalbialek.com collects, why, and your rights under the GDPR.", privacy_en, "polityka-prywatnosci/"),
    ("regulamin/", "pl", "Regulamin serwisu | Michał Białek", "Zasady korzystania z serwisu michalbialek.com i formularza kontaktowego.", terms_pl, "en/terms/"),
    ("en/terms/", "en", "Website terms | Michał Białek", "Rules for using michalbialek.com and its contact form.", terms_en, "regulamin/"),
]

CSS = """
:root{--bg:#ECEFF3;--surface:#F8F9FB;--ink:#0D1726;--muted:#566275;--line:#C9D0DA;--accent:#2A43DB}
@media (prefers-color-scheme: dark){:root{--bg:#0A1019;--surface:#111925;--ink:#E5EAF1;--muted:#8E9AAD;--line:#223047;--accent:#7D8DFF}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 "Instrument Sans",system-ui,sans-serif}
a{color:var(--accent)}
.top{border-bottom:1px solid var(--line);background:var(--surface)}
.wrap{max-width:780px;margin:0 auto;padding:0 20px}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;height:64px}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font:700 1.05rem "Schibsted Grotesk",system-ui,sans-serif}
.brand img{width:34px;height:34px}
.top nav{display:flex;gap:16px;font-size:.92rem}
.top nav a{color:var(--muted);text-decoration:none;white-space:nowrap}
.brand{white-space:nowrap}
@media (max-width:480px){.top nav a.home{display:none}}
.top nav a:hover{color:var(--ink)}
main{padding:40px 0 64px}
h1{font:800 clamp(1.9rem,5vw,2.6rem)/1.15 "Schibsted Grotesk",system-ui,sans-serif;margin:0 0 6px;letter-spacing:-.02em}
h2{font:700 1.25rem/1.3 "Schibsted Grotesk",system-ui,sans-serif;margin:36px 0 8px}
h3{font-size:1rem;margin:20px 0 4px}
.upd{font:400 .8rem "JetBrains Mono",ui-monospace,monospace;color:var(--muted);margin:0 0 24px}
ul{padding-left:1.2em}li{margin:4px 0}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:.88rem}
footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;padding-block:24px}
footer a{color:inherit}
"""

def page(path, lang, title, desc, body_fn, alt):
    pl_path, en_path = (path, alt) if lang == "pl" else (alt, path)
    home = "/" if lang == "pl" else "/en/"
    nav = ('<a class="home" href="/">Strona główna</a><a href="/#kontakt">Kontakt</a><a href="/%s" hreflang="en">EN</a>' % alt) if lang == "pl" else \
          ('<a class="home" href="/en/">Home</a><a href="/en/#kontakt">Contact</a><a href="/%s" hreflang="pl">PL</a>' % alt)
    links = ('<a href="/polityka-prywatnosci/">Polityka prywatności</a> · <a href="/regulamin/">Regulamin</a>') if lang == "pl" else \
            ('<a href="/en/privacy-policy/">Privacy policy</a> · <a href="/en/terms/">Terms</a>')
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE}/{path}">
<link rel="alternate" hreflang="pl" href="{SITE}/{pl_path}">
<link rel="alternate" hreflang="en" href="{SITE}/{en_path}">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/assets/fonts/fonts.css">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{home}"><img src="/assets/favicon.svg" alt="">Michał Białek</a>
<nav>{nav}</nav>
</div></header>
<main><div class="wrap">{body_fn()}</div></main>
<footer><div class="wrap"><span>© 2026 Michał Białek · {links}</span><span>{EMAIL}</span></div></footer>
</body>
</html>
"""

def build(root):
    for path, lang, title, desc, fn, alt in PAGES:
        d = root / path
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(path, lang, title, desc, fn, alt), encoding="utf-8")
    return [(p, l, a) for p, l, _, _, _, a in PAGES]
