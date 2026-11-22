# Projekt 04 – DevSecOps: bezpieczne wdrażanie aplikacji Edge–Cloud

**WSTI, Projekt Zespołowy: Bezpieczna Infrastruktura Hybrydowa z AI (2026/2027)**  
**Pakiet:** M1 + M2 (plan, dokumentacja, szkielet PoC).  
**Status:** propozycja do zatwierdzenia; testy CI, skan, publikacja GHCR i wdrożenie **nie zostały zweryfikowane**.  
**Zespół:** planowane **5 osób** – **wymagana zgoda prowadzącego**, ponieważ źródłowe dokumenty zakładają zespoły 4-osobowe.

## Zacznij tutaj

1. Uzupełnij [kartę M1](docs/M1/01-karta-projektu.md): nazwiska 5 osób, repozytorium, potwierdzenie zmiany liczebności.
2. Przejrzyj [role i ślad wkładu](docs/M1/02-role-i-komunikacja.md), [plan sprintu](docs/M1/03-plan-pierwszego-sprintu.md) i [checklistę M1](docs/M1/04-checklista-M1.md).
3. Zaprezentuj [architekturę](docs/M2/02-architektura.md), [DFD](docs/M2/03-przeplyw-danych.md), [STRIDE](docs/M2/04-model-zagrozen-STRIDE.md), [rejestr ryzyk](docs/M2/05-rejestr-ryzyk.md) oraz [backlog](docs/M2/06-backlog.md).
4. Przejdź przez [checklistę M2](docs/M2/09-checklista-odbioru.md) i [prezentację](docs/M2/12-prezentacja-M2.md).
5. Uruchom PoC według [instrukcji i szablonu dowodów](docs/M2/08-PoC-i-dowody.md). Uzupełnij prawdziwe logi i linki – nie wpisuj hipotetycznych sukcesów.

## Wymagania źródłowe

| Etap | Data | Zawartość |
|---|---|---|
| M1 | 16.10.2026 | Zespół, role, karta projektu, repozytorium |
| M2 | 27.11.2026 | Diagram, przepływ danych, model zagrożeń, backlog; dodatkowo PoC |

Plan przedmiotu: `sources/WSTI_PZBI_plan_przedmiotu.pdf`.  
Katalog tematów, projekt 04: `sources/WSTI_PZBI_katalog_8_projektow.pdf`.

## Zawartość repozytorium

```text
.
├── README.md
├── docs/
│   ├── M1/
│   │   ├── 01-karta-projektu.md
│   │   ├── 02-role-i-komunikacja.md
│   │   ├── 03-plan-pierwszego-sprintu.md
│   │   └── 04-checklista-M1.md
│   └── M2/
│       ├── 02-architektura.md
│       ├── 03-przeplyw-danych.md
│       ├── 04-model-zagrozen-STRIDE.md
│       ├── 05-rejestr-ryzyk.md
│       ├── 06-backlog.md
│       ├── 07-decyzje-ADR.md
│       ├── 08-PoC-i-dowody.md
│       ├── 09-checklista-odbioru.md
│       ├── 10-plan-AI-ML.md
│       ├── 11-macierz-wymagan.md
│       └── 12-prezentacja-M2.md
├── .github/workflows/ci.yml
├── app/                  # Minimalna demonstracyjna FastAPI
├── tests/                # Szkielet testów
├── infrastructure/       # Plan infrastruktury do M3
├── monitoring/           # Plan telemetrii do M4
├── sources/              # PDF-y prowadzącego
├── Dockerfile
├── compose.poc.yaml
├── requirements.txt
└── requirements-dev.txt
```

## Propozycja techniczna (nie narzucona przez prowadzącego)

- GitHub + Actions + GHCR; FastAPI i Docker/Compose.
- SAST/SCA: Semgrep, Trivy; skan sekretów Gitleaks; SBOM Syft.
- Edge: oddzielna VM; Cloud: oddzielna VM dla monitoringu/AI; możliwa symulacja na lokalnym Proxmox.
- Monitoring: Prometheus/Grafana, wyniki pipeline + metryki aplikacji, AI/ML z oceną jakości.

## Uruchomienie lokalnego szkieletu

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
pytest -q
uvicorn app.main:app --host 127.0.0.1 --port 8003
# w osobnym terminalu:
curl http://127.0.0.1:8003/health
```

CI i GHCR wymagają konfiguracji repozytorium/permissions. Testy na żywym GitHub i Edge nie zostały wykonane w trakcie przygotowania pakietu.

## Uczciwy status

- **Przygotowano:** dokumenty, diagramy Markdown/Mermaid, wstępne STRIDE/DFD/backlog, kod/szkielet PoC.
- **Do wykonania:** personalizacja 5-osobowego składu i akceptacja prowadzącego, faktyczne repo, wykonanie CI i zapis dowodów.
- **Etapy późniejsze:** automatyczny Edge deploy i rollback oraz rzeczywisty monitoring i AI/ML.

Testy wykonywać wyłącznie na własnej odizolowanej infrastrukturze i danych syntetycznych.


## Zweryfikowane testy lokalne – 22.11.2026

- **pytest:** 2/2 PASS, 3 ostrzeżenia deprecacyjne.
- **FastAPI:** poprawne uruchomienie na `127.0.0.1:8003`.
- **GitHub Actions / Trivy / GHCR / Edge:** do weryfikacji.
- [Protokół testowy M2](docs/M2/13-testy-lokalne-2026-11-22.md).

### Uruchomienie

```bash
./run-local.sh
```

- API: http://127.0.0.1:8003
- Swagger: http://127.0.0.1:8003/docs
- Health: http://127.0.0.1:8003/health
