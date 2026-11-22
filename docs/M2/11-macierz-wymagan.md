# M2-11. Macierz wymagań – SmartGate / temat 04

| Źródło | Wymaganie | Artefakt | Etap/status |
|---|---|---|---|
| Plan §4 | M2: architektura, DFD, STRIDE i backlog | 02–06 | M2: opracowane |
| Plan §7 | dowód wykonalności | [Dowody](08-PoC-i-dowody.md) | M2: API i CI zweryfikowane |
| Plan §5 | 2 rozdzielone logicznie warstwy Edge/Cloud | 02,03 | M3: planowane |
| Katalog nr 04 | build + test + deploy | `.github/workflows/ci.yml`, M3 | CI i publikacja działają; wdrożenie na Edge w M3 |
| Katalog nr 04 | SAST, SCA, image scan, critical gate | CI, STRIDE | skany przeszły; kontrolowana blokada CRITICAL do sprawdzenia |
| Katalog nr 04 | SBOM/podpis/manifest | workflow | SBOM wygenerowany w #8 |
| Katalog nr 04 | rollback i audyt | backlog M3/M5 | planowane |
| Plan §5 | auth, szyfrowanie, sekrety, RBAC | STRIDE, ADR, backlog | demonstracyjne API key, reszta planowana |
| Plan §5 | dwa źródła telemetrii | AI plan | M4: planowane |
| Plan §5 | AI/ML z metryką i baseline | AI plan | M4: planowane |
| SmartGate – wybór zespołu | fikcyjna tablica i lokalna decyzja | `app/main.py`, `app/parking.py`, testy | potwierdzone testami i demonstracją API |
| SmartGate – wybór zespołu | lokalna decyzja bez usługi Cloud, raport co minutę | architektura, backlog | lokalna decyzja działa; raport w M3 |

Ważne: **SmartGate jest demonstratorem**, a celem ocenianym w temacie 04 jest zabezpieczony pipeline DevSecOps i integracja Edge–Cloud.
