# SmartGate DevSecOps

Projekt zespołowy WSTI, temat 04: bezpieczne wdrażanie aplikacji Edge–Cloud.

SmartGate to symulator wjazdu na parking. Podajemy fikcyjny numer rejestracyjny. Aplikacja sprawdza abonament w lokalnej bazie SQLite, zwraca `OPEN` albo `DENY` i zapisuje zdarzenie. Na tym przykładzie pokazujemy, jak sprawdzić kod i obraz przed wdrożeniem.

## Materiały do przeglądu

- **M1** — [karta projektu](docs/M1/01-karta-projektu.md), [skład, role i wykonane prace](docs/M1/02-role-i-komunikacja.md), [plan sprintu](docs/M1/03-plan-pierwszego-sprintu.md).
- **M2** — [przegląd materiałów](docs/M2/01-przeglad-M2.md), [dowody działania](docs/M2/08-PoC-i-dowody.md). Raport postępu jest osobnym PDF-em.
- [Materiały WSTI](sources/README.md).

## Stan na M2

Działa lokalne API SmartGate. GitHub Actions uruchamia testy i skany, buduje obraz, zapisuje listę jego składników (SBOM) i publikuje obraz w GHCR. W [przebiegu #13](https://github.com/pniewrzol/DevSecOps-Edge-Cloud-app/actions/runs/45615818687) przeszły oba zadania, także publikacja.

Na następny etap planujemy uruchomienie obrazu na VM Edge i przesłanie raportu do VM Cloud. [Infrastruktura](infrastructure/README.md) opisuje układ maszyn, a [plan monitoringu](docs/M2/10-plan-AI-ML.md) porównuje dwa warianty.

## Uruchomienie lokalne (Linux)

W katalogu repozytorium uruchom:

```bash
bash ./run-local.sh
```

Skrypt tworzy środowisko Pythona, uruchamia testy i startuje serwer. W drugim terminalu wpisz:

```bash
bash ./run-local.sh check
curl -fsS http://127.0.0.1:8003/api/v1/access/check \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: local-demo-only-change-me' \
  -d '{"plate":"SK 12345"}'
```

Dokumentacja API działa pod adresem `http://127.0.0.1:8003/docs`. Tablica `SK 12345` daje `OPEN`, `KR 98765` daje `DENY`, a `SB 2026A` ma wygasły abonament. Klucz w przykładzie służy wyłącznie do lokalnego demo. Baza jest zapisywana w `.local/`.

## Uruchomienie przez Docker Compose

Zatrzymaj lokalny serwer przed startem kontenera. Obie wersje używają portu 8003.

```bash
export SMARTGATE_API_KEY="$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')"
docker compose -f compose.poc.yaml up --build -d
docker compose -f compose.poc.yaml ps
curl -fsS http://127.0.0.1:8003/health
docker compose -f compose.poc.yaml down
```

Compose buduje obraz lokalnie i zapisuje bazę w woluminie `smartgate-data`. Do demonstracji używaj fikcyjnych tablic.
