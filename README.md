# SmartGate DevSecOps – bezpieczne wdrażanie aplikacji Edge–Cloud

**WSTI, temat 04: DevSecOps – bezpieczne wdrażanie aplikacji Edge–Cloud** · M1/M2 · 2026/2027.

> **Stan:** lokalny szkielet aplikacji SmartGate został zaimplementowany; nowy zestaw testów musi przejść w środowisku zespołu i GitHub Actions. Synchronizacja Cloud, monitorowanie AI/ML, automatyczny Edge deploy i rollback to **planowane etapy M3–M5**, a nie funkcje gotowe.

## Cel

SmartGate to **symulator lokalnego szlabanu parkingowego** (bez fizycznego sterowania). Przyjmuje fikcyjny numer rejestracyjny, weryfikuje uprawnienie w lokalnej bazie SQLite, zwraca `OPEN` lub `DENY`, a historię zdarzeń zapisuje lokalnie. Docelowo co minutę będzie przekazywał raport do Cloud i odbierał kontrolowane aktualizacje uprawnień. Przy braku Internetu Edge ma działać z lokalną kopią danych i buforować zdarzenia. Najważniejszym celem przedmiotu jest jednak **bezpieczny proces CI/CD** od kodu poprzez testy i skany aż do wdrożenia/rollbacku.

**Zespół:** Patryk – lider / architekt; Michał i Kamil – Cloud/DevOps; Kajetan – Security; Bartek – AI/Monitoring. Pięć osób zgodne z informacją zespołu o dopuszczalnym maksimum; formalne potwierdzenie statusu z prowadzącym: **[DO UZUPEŁNIENIA]**.

## Uruchomienie lokalne (Linux)

```bash
chmod +x run-local.sh
./run-local.sh          # środowisko, pytest, serwer na 127.0.0.1:8003
```

- API: http://127.0.0.1:8003
- Dokumentacja Swagger: http://127.0.0.1:8003/docs
- Healthcheck: http://127.0.0.1:8003/health
- Lokalny klucz demonstracyjny (TYLKO `127.0.0.1`): `local-demo-only-change-me`. Użyj własnego `SMARTGATE_API_KEY` poza tą demonstracją.

```bash
curl -s -X POST http://127.0.0.1:8003/api/v1/access/check \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: local-demo-only-change-me' \
  -d '{"plate":"SK 12345"}'
# przykład: {"plate":"SK12345","decision":"OPEN","reason":"active_permit","simulated":true}
```

Przykładowe syntetyczne tablice: `SK 12345` – aktywna, `KR 98765` – nieaktywna, `SB 2026A` – wygasła. Brak prawdziwych danych osobowych. Logika decyzji jest deterministyczna; AI nie może otwierać szlabanu.

## Uruchomienie przez Docker Compose

```bash
export SMARTGATE_API_KEY="$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')"
docker compose -f compose.poc.yaml up --build -d
curl http://127.0.0.1:8003/health
docker compose -f compose.poc.yaml down
```

**Nie uruchamiaj jednocześnie wersji lokalnej i kontenerowej na porcie 8003.** Lokalna SQLite jest w `.local/`, kontenerowa w trwałym woluminie `smartgate-data`. Wersja demo nie posiada produkcyjnego mechanizmu rotacji kluczy, centralnego uwierzytelnienia ani synchronizacji abonamentów.

## Dokumentacja etapów

- [M1 – karta projektu](docs/M1/01-karta-projektu.md) · [role](docs/M1/02-role-i-komunikacja.md) · [sprint](docs/M1/03-plan-pierwszego-sprintu.md) · [checklista](docs/M1/04-checklista-M1.md)
- [M2 – architektura](docs/M2/02-architektura.md) · [DFD](docs/M2/03-przeplyw-danych.md) · [STRIDE](docs/M2/04-model-zagrozen-STRIDE.md) · [ryzyka](docs/M2/05-rejestr-ryzyk.md) · [backlog](docs/M2/06-backlog.md)
- [ADR](docs/M2/07-decyzje-ADR.md) · [PoC/dowody](docs/M2/08-PoC-i-dowody.md) · [AI/ML](docs/M2/10-plan-AI-ML.md) · [wymagania](docs/M2/11-macierz-wymagan.md) · [scenariusz M2](docs/M2/12-prezentacja-M2.md)
- [Historyczne testy poprzedniego szkieletu](docs/M2/13-testy-lokalne-2026-11-22.md) · [Migracja i audyt](docs/M2/14-audyt-migracji-smartgate.md)

## Status weryfikacji

| Obszar | Stan |
|---|---|
| Lokalny szkielet FastAPI (poprzednia wersja) | 2/2 testów PASS (log 22.11.2026), port 8003 |
| Nowa logika SmartGate | Kod i testy przygotowane; wynik w CI do potwierdzenia |
| GitHub Actions | Ostatni sprawdzony run `0c52d7d` nieudany na kroku Tests, dalsze kroki pominięte |
| SAST/SCA/SBOM/GHCR | Definicja pipeline; skuteczne wykonanie do udokumentowania |
| Edge–Cloud sync i rollback | Planowane M3–M5 |
| Monitoring i AI/ML | Planowane M4 |

Źródła wymagań: `sources/`. Testy demonstracyjne tylko na własnym izolowanym środowisku.
