# M2-11. Macierz wymagań – SmartGate / temat 04

| Źródło | Wymaganie | Artefakt | Etap/status |
|---|---|---|---|
| Plan §4 | M2: architektura, DFD, STRIDE i backlog | 02–06 | M2: projektowane |
| Plan §7 | dowód wykonalności | 08,13,14 | lokalne stare 2/2, nowy PoC do sprawdzenia |
| Plan §5 | 2 rozdzielone logicznie warstwy Edge/Cloud | 02,03 | M3: planowane |
| Katalog nr 04 | build + test + deploy | `.github/workflows/ci.yml`, M3 | CI do naprawy, Edge deploy planowany |
| Katalog nr 04 | SAST, SCA, image scan, critical gate | CI, STRIDE | CI do zweryfikowania |
| Katalog nr 04 | SBOM/podpis/manifest | workflow | generowanie zdefiniowane, wynik do potwierdzenia |
| Katalog nr 04 | rollback i audyt | backlog M3/M5 | planowane |
| Plan §5 | auth, szyfrowanie, sekrety, RBAC | STRIDE, ADR, backlog | demonstracyjne API key, reszta planowana |
| Plan §5 | dwa źródła telemetrii | AI plan | M4: planowane |
| Plan §5 | AI/ML z metryką i baseline | AI plan | M4: planowane |
| SmartGate – wybór zespołu | fikcyjna tablica i lokalna decyzja | `app/main.py`, `app/parking.py`, testy | przygotowano kod, do weryfikacji CI |
| SmartGate – wybór zespołu | działanie offline, raport co minutę | architektura, backlog | M3: planowane |

Ważne: **SmartGate jest demonstratorem**, a celem ocenianym w temacie 04 jest zabezpieczony pipeline DevSecOps i integracja Edge–Cloud.
