# michalbialek.com

Strona firmowa (PL/EN): oprogramowanie na zamówienie, automatyzacja, integracje i optymalizacja.

## Struktura
- `src/page.html` – źródło strony (treści PL w HTML, tłumaczenia EN w słowniku `EN` w skrypcie).
- `index.html` – gotowa strona do wgrania na hosting; generowana z `src/page.html`.
- `assets/` – logo i ikony używane przez stronę.
- `logo/` – wszystkie warianty logo (SVG) i skrypt `generuj_logo.py`.

## Zmiana treści
1. Edytuj `src/page.html`.
2. Uruchom `python3 build.py`, żeby odświeżyć `index.html`.
3. Wgraj `index.html` i folder `assets/` do katalogu `www` na hostingu OVH.

## Ustawienia (na początku skryptu w `src/page.html`)
- `CONTACT` – e-mail, telefon, LinkedIn, GitHub, adres biura.
- `WEB3FORMS_KEY` – klucz formularza kontaktowego z https://web3forms.com (pusty = tryb podglądu).
