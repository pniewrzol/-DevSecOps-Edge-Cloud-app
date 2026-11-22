# M2-08. PoC SmartGate – plan i dowody

## Stan aktualny

- 22.11.2026: **historyczny szkielet** FastAPI przeszedł lokalnie 2/2 testów, 3 warnings, Uvicorn na porcie 8003 ([protokół](13-testy-lokalne-2026-11-22.md)). To nie są testy logiki SmartGate.
- GitHub Actions run `45059847478` dla commitu `0c52d7d`: FAILED w `Tests`, Semgrep/Trivy/build/publish pominięte – <https://github.com/pniewrzol/-DevSecOps-Edge-Cloud-app/actions/runs/45059847478>.
- Zmieniono workflow na `python -m pytest -q` jako potencjalne rozwiązanie błędu importu z katalogu root; **wymaga sprawdzenia w CI**.
- Nowy symulator SmartGate implementuje lokalne decyzje, SQLite, zdarzenia i demonstracyjne uwierzytelnienie API key. Nie realizuje jeszcze synchronizacji Cloud ani automatycznego deploy.

## Testy do wykonania na nowym kodzie

```bash
./run-local.sh test
./run-local.sh start
# drugi terminal
curl http://127.0.0.1:8003/health
curl -X POST http://127.0.0.1:8003/api/v1/access/check \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: local-demo-only-change-me' \
  -d '{"plate":"SK 12345"}'
```

## Dowody M2 – uzupełnić po uruchomieniu

| ID | Dowód | Status |
|---|---|---|
| E01 | Testy nowego SmartGate pytest | WYMAGA POTWIERDZENIA / LOGU |
| E02 | API: aktywny abonament daje OPEN | WYMAGA POTWIERDZENIA / LOGU |
| E03 | API: brak klucza daje 401 | WYMAGA POTWIERDZENIA / LOGU |
| E04 | CI: green build/test, skany Semgrep i Trivy | WYMAGA RUNU |
| E05 | CI: SBOM + GHCR | WYMAGA RUNU |
| E06 | Kontrolowana blokada CRITICAL | WYMAGA RUNU |

Nie podpisywać jako wykonane dowodów, których nie ma. Zamieścić ID joba, SHA, logi/zrzuty i daty.
