# M2 – Protokół testów lokalnych

**Data:** 22.11.2026
**Status:** ZALICZONE – testy lokalne

## Środowisko

- System: Linux (EndeavourOS)
- Python: 3.14.10
- pytest: 8.3.5
- Port aplikacji: 8003
- Adres: http://127.0.0.1:8003

## Wyniki

| Test | Wynik |
|---|---|
| tests/test_app.py::test_health | PASS |
| tests/test_app.py::test_root | PASS |
| Uvicorn – Application startup complete | OK |
| Test HTTP curl /health | Do osobnego potwierdzenia |
| GitHub Actions | Niezweryfikowane |
| Trivy / GHCR | Niezweryfikowane |

**Podsumowanie pytest:** 2 passed, 3 warnings in 0.14s.

Trzy ostrzeżenia DeprecationWarning dotyczą bibliotek
Starlette/AnyIO i FastAPI oraz zgodności z przyszłymi
wersjami Pythona. Nie spowodowały niepowodzenia testów.

**Źródło:** log terminala dostarczony przez wykonawcę.

## Wnioski

Testy jednostkowe zakończyły się sukcesem, a serwer
aplikacji FastAPI uruchomił się poprawnie na porcie 8003.

Nie oznacza to jeszcze zaliczenia pełnego PoC CI/CD.
