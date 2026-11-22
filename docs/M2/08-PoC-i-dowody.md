# M2-08. Proof of Concept i dowody wykonalności

**Cel M2:** pokazać wykonalność kluczowego etapu: automatyczny test → build obrazu → skan zależności/obrazu → bramka `CRITICAL` → publikacja do GHCR (tylko na zaufanym branchu). **Status:** testy lokalne pytest 2/2 PASS i start serwera 8003 potwierdzone logiem 22.11.2026; CI/GHCR i skany NIEZWERYFIKOWANE. [Protokół](13-testy-lokalne-2026-11-22.md).

## Wymagania PoC

- Repozytorium z włączonym GitHub Actions.
- Uprawnienia `GITHUB_TOKEN` do zapisu pakietów tylko dla joba publikacji w `main`; PR bez poświadczeń deploymentowych.
- Dockerfile aplikacji i co najmniej jeden test pytest.
- Skan kodu (Semgrep) i zależności (Trivy fs), skan obrazu (Trivy image) z bramką critical.
- Artefakt SBOM; publikacja obrazu po przejściu kontroli.

## Kroki lokalne

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
pytest -q
python -m uvicorn app.main:app --host 127.0.0.1 --port 8003
# w osobnej konsoli
curl -f http://127.0.0.1:8003/health
```

## Kroki CI

1. Wypchnąć na własny branch i otworzyć PR: zweryfikować testy i skanowanie bez publikacji do registry.
2. Po review wykonać merge do `main`: zweryfikować raporty, SBOM i opublikowany obraz w GHCR.
3. Przygotować **kontrolowany test blokady** (np. odrębny branch i reguła testowa / skan podatnego artefaktu z potwierdzonym wynikiem CRITICAL). Nie wprowadzać niebezpiecznego komponentu do wydania głównego.
4. Zweryfikować, że pipeline z CRITICAL nie uruchamia kroku publikacji.

**Uwaga:** demo włączenia realnego `CRITICAL` może zależeć od aktualnej bazy CVE; można dodatkowo sprawdzić logikę policy gate przez kontrolowany fixture raportu, ale należy wyraźnie oznaczyć symulację.

## Formularz dowodów (uzupełnić po wykonaniu)

| ID | Dowód | Link/ścieżka | Wynik | Data |
|---|---|---|---|---|
| E01 | Run udanego PR: test + skany | [DO UZUPEŁNIENIA] | NIE WYKONANO | – |
| E02 | Run main i publikacja GHCR | [DO UZUPEŁNIENIA] | NIE WYKONANO | – |
| E03 | SBOM z poprawnego pipeline | [DO UZUPEŁNIENIA] | NIE WYKONANO | – |
| E04 | Run z zablokowanym CRITICAL | [DO UZUPEŁNIENIA] | NIE WYKONANO | – |
| E05 | Log decyzji policy gate | [DO UZUPEŁNIENIA] | NIE WYKONANO | – |

## Oczekiwane kryteria sukcesu

- Przynajmniej jeden autentyczny zielony run i jeden kontrolowany odrzucony run (jeśli możliwe przed M2).
- Brak sekretów w repozytorium i outputach.
- Ślad łączący obraz OCI z SHA commitu oraz wynikami testów.
- Wyraźna informacja: deployment do Edge i rollback będą dopiero w M3/M5.
