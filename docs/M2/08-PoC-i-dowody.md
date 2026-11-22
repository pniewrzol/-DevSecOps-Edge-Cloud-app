# M2 – Dowody wykonalności SmartGate

W M2 sprawdziliśmy dwa kluczowe elementy: lokalną decyzję parkingową w oparciu o SQLite oraz potok od testów i skanowania do publikacji obrazu.

| Dowód z 22.11.2026 | Wynik |
|---|---|
| `python -m pytest -q` | 10 testów zaliczonych. Jedno ostrzeżenie o przestarzałym API Starlette/AnyIO. |
| Uruchomione API i tymczasowa baza SQLite | `GET /health`: 200. Fikcyjna tablica `SK 12345`: `OPEN`; `KR 98765`: `DENY`; bez klucza: 401. Podsumowanie: po jednym `OPEN` i `DENY`, dwa zdarzenia oczekujące. |
| [GitHub Actions #8](https://github.com/pniewrzol/-DevSecOps-Edge-Cloud-app/actions/runs/45068382402), commit `10915b9` | Przeszły testy, Semgrep, skan zależności i skan obrazu Trivy. CI wygenerowało i zapisało SBOM CycloneDX jako artefakt przebiegu. |
| Publikacja obrazu w tym samym przebiegu | `ghcr.io/pniewrzol/smartgate-edge:10915b9787c9cad4709bef2288e630e245165a8c` |

## Demonstracja

Uruchom aplikację według [README](../../README.md#uruchomienie-lokalne-linux), pokaż wynik sprawdzenia fikcyjnej tablicy i powtórz żądanie bez nagłówka `X-API-Key`. Następnie otwórz przebieg #8 i pokaż zadanie publikacji oraz artefakt `sbom-cyclonedx`.

## Kolejny etap

Potok skanuje obraz w pierwszym zadaniu, a zadanie publikacji buduje go ponownie z tego samego commita. Przed wdrożeniem Edge trzeba publikować ten sam obraz, który przeszedł skan, i weryfikować jego digest. Kontrolowana blokada dla wyniku CRITICAL, raportowanie do Cloud i próba rollbacku pozostają w [backlogu](06-backlog.md).
