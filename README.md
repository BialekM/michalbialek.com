# michalbialek.com

Strona firmowa (PL/EN): oprogramowanie na zamówienie, automatyzacja, integracje i optymalizacja.

## Struktura
- `src/page.html` – źródło strony (treści PL w HTML, tłumaczenia EN w słowniku `EN` w skrypcie).
- `index.html` – gotowa strona do wgrania na hosting; generowana z `src/page.html`.
- `assets/` – logo i ikony używane przez stronę.
- `logo/` – wszystkie warianty logo (SVG) i skrypt `generuj_logo.py`.

## Zmiana treści
1. Edytuj `src/page.html`.
2. Wypchnij zmiany na gałąź `main`. GitHub Actions sam zbuduje `index.html` i wyśle stronę na OVH (folder `www`).
3. Lokalny podgląd: `python3 build.py`, potem otwórz `index.html` w przeglądarce.

## Automatyczne wdrożenie (GitHub Actions → OVH)
Workflow: `.github/workflows/deploy.yml`. Wymaga trzech sekretów w **Settings → Secrets and variables → Actions**:
- `FTP_SERVER` – adres serwera FTP z panelu OVH (zakładka FTP-SSH), np. `ftp.clusterXXX.hosting.ovh.net`
- `FTP_USERNAME` – login FTP
- `FTP_PASSWORD` – hasło FTP

Ręczne uruchomienie: zakładka **Actions → Wdrożenie na OVH → Run workflow**.

## Ustawienia (na początku skryptu w `src/page.html`)
- `CONTACT` – e-mail, telefon, LinkedIn, GitHub, adres biura.
- `WEB3FORMS_KEY` – klucz formularza kontaktowego z https://web3forms.com (pusty = tryb podglądu).
