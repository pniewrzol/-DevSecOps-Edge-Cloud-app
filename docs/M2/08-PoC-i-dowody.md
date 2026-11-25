# M2 – Dowody działania

| Sprawdzenie | Wynik |
|---|---|
| Testy lokalne 22.11.2026 | `python -m pytest -q`: 10 zaliczonych testów. Jedno ostrzeżenie o przestarzałym API Starlette/AnyIO. |
| Uruchomienie API | `GET /health` zwrócił HTTP 200. `SK 12345` dało `OPEN`, `KR 98765` dało `DENY`. Brak klucza dał HTTP 401. Podsumowanie pokazało po jednej decyzji i dwa zdarzenia oczekujące na wysyłkę. |
| [GitHub Actions #8](https://github.com/pniewrzol/-DevSecOps-Edge-Cloud-app/actions/runs/45068382402) | Przeszły testy, Semgrep, skan zależności i skan obrazu Trivy. SBOM CycloneDX zapisano jako artefakt. |
| Publikacja w przebiegu #8 | `ghcr.io/pniewrzol/smartgate-edge:10915b9787c9cad4709bef2288e630e245165a8c` |

Aby powtórzyć próbę, uruchom SmartGate według [README](../../README.md#uruchomienie-lokalne-linux). W `/docs` możesz pokazać decyzje dla dwóch tablic i powtórzyć żądanie bez klucza. W GitHub Actions pokaż artefakt `sbom-cyclonedx` i zadanie publikacji.

W obecnym potoku obraz został zeskanowany w pierwszym zadaniu, a zadanie publikacji zbudowało go ponownie z tego samego commita. Wdrożenie po digescie dokładnie zeskanowanego obrazu i kontrolowana próba blokady `CRITICAL` są w [backlogu](06-backlog.md).
