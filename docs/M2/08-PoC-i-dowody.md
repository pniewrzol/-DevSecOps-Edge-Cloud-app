# M2 – Dowody działania

| Sprawdzenie | Wynik |
|---|---|
| Testy lokalne 22.11.2026 | `python -m pytest -q`: 10 zaliczonych testów. Jedno ostrzeżenie o przestarzałym API Starlette/AnyIO. |
| Uruchomienie API | `GET /health` zwrócił HTTP 200. `SK 12345` dało `OPEN`, `KR 98765` dało `DENY`. Brak klucza dał HTTP 401. Podsumowanie pokazało po jednej decyzji i dwa zdarzenia oczekujące na wysyłkę. |
| [GitHub Actions #13](https://github.com/pniewrzol/DevSecOps-Edge-Cloud-app/actions/runs/45615818687) | Przeszły testy, Semgrep, skan zależności i skan obrazu Trivy. SBOM CycloneDX zapisano jako artefakt. |
| Publikacja w przebiegu #13 | `ghcr.io/pniewrzol/smartgate-edge:d48babf4abbbe1ebb8c49871c263d4bd99661d43` |

Aby powtórzyć próbę, uruchom SmartGate według [README](../../README.md#uruchomienie-lokalne-linux). W `/docs` możesz pokazać decyzje dla dwóch tablic i powtórzyć żądanie bez klucza. W GitHub Actions pokaż artefakt `sbom-cyclonedx` i zadanie publikacji.

W obecnym potoku obraz został zeskanowany w pierwszym zadaniu, a zadanie publikacji zbudowało go ponownie z tego samego commita. Wdrożenie po digescie dokładnie zeskanowanego obrazu i kontrolowana próba blokady `CRITICAL` są w [backlogu](06-backlog.md).
