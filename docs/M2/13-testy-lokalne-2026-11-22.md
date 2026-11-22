# M2 – Wyniki testów lokalnych

**Data:** 22.11.2026  
**Wykonawca:** Patryk (log terminala przekazany w rozmowie)  
**Środowisko:** EndeavourOS Linux, Python 3.14.10, pytest 8.3.5  
**Uruchomienie:** `./run-local.sh`  
**Adres:** http://127.0.0.1:8003

| Sprawdzenie | Wynik |
|---|---|
| `tests/test_app.py::test_health` | **PASS** |
| `tests/test_app.py::test_root` | **PASS** |
| Uruchomienie Uvicorn na porcie 8003 | **OK** (`Application startup complete`) |
| Oddzielny HTTP healthcheck z innego terminala | **Niepotwierdzony** |
| GitHub Actions, skan Trivy, GHCR | **Niepotwierdzone** |
| Edge deployment, rollback | **Niepotwierdzone** |

Podsumowanie: **2 passed, 3 warnings in 0.14s**. Ostrzeżenia deprecacyjne dotyczą Starlette/AnyIO i FastAPI; nie są błędami testów. Wyniki te potwierdzają wyłącznie lokalny test i start API, nie kompletny proces CI/CD.
