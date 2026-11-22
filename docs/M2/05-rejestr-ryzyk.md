# M2-05. Rejestr ryzyk SmartGate DevSecOps

**Metoda:** P = prawdopodobieństwo 1–3; I = wpływ 1–3; R=P×I (1–2 niskie, 3–4 średnie, 6–9 wysokie). Szacunki bez wyników testów. Weryfikować przy każdym sprint review.

| ID | Ryzyko | P | I | R | Redukcja | Właściciel | Weryfikacja |
|---|---|---:|---:|---:|---|---|---|
| R01 | Nieautoryzowana zmiana abonamentów | 2 | 3 | 6 | kontrola wersji/sygnatur i uprawnień | Kajetan / Kamil | test odmowy i integralności |
| R02 | Fałszywa decyzja OPEN | 2 | 3 | 6 | fail-closed dla braku/wygaśnięcia, walidacja danych | Kajetan | test nieznanej/nieaktywnej tablicy |
| R03 | Przerwa Internetu i utrata raportów | 3 | 2 | 6 | lokalny SQLite outbox + retry/idempotencja | Kamil | test odłączenia Cloud |
| R04 | Nieaktualne uprawnienia offline | 2 | 3 | 6 | limity ważności snapshotu, polityka revocation | Patryk / Kajetan | test wygasłego snapshotu |
| R05 | Wyciek tokenu CI lub API key | 2 | 3 | 6 | secrets management, least privilege, review | Kajetan / Michał | skan i audyt permissions |
| R06 | Podatny / podmieniony obraz | 2 | 3 | 6 | Trivy, SBOM, digest i policy gate | Michał / Kajetan | zablokowany run CI |
| R07 | Wadliwe wdrożenie | 2 | 3 | 6 | healthcheck, last-known-good, rollback | Kamil | kontrolowana awaria |
| R08 | Niepoprawny model ML | 2 | 2 | 4 | baseline, niezależny test, precision/recall/F1 | Bartek | raport M4 |
| R09 | Zbyt szeroki zakres do M4 | 3 | 3 | 9 | najpierw M2 dokumenty i M3 minimalny end-to-end | Patryk | sprint review |
| R10 | Ujawnienie numerów rejestracyjnych | 2 | 2 | 4 | fikcyjne dane, minimalizacja i retencja | Kajetan / Bartek | przegląd logów i raportów |

**Najważniejsze dla M2:** R01, R05, R06, R09. Akceptację ryzyka wysokiego dokumentują Patryk i Kajetan; nie wpisujemy fikcyjnych zatwierdzeń.
