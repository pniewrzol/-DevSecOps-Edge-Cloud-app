# M1 – Role, komunikacja i ślad wkładu (5 osób)

**Uzgodniony podział zespołu (22.11.2026) – projekt SmartGate DevSecOps:** Patryk – lider / architekt; Michał i Kamil – Cloud / DevOps; Kajetan – Security Engineer; Bartek – AI / Monitoring.

Prowadzący zaakceptował pięcioosobowy skład. Michał odpowiada za CI/CD, a Kamil za środowisko wdrożeniowe i synchronizację.

## Macierz RACI

R = realizuje, A = odpowiada za wynik, C = konsultowany, I = informowany. W każdym wierszu jest jedna osoba A. Osoby Michał i Kamil współpracują przy Cloud / DevOps, z wyraźnym właścicielem danego zadania.

| Obszar | Patryk | Michał | Kamil | Kajetan | Bartek |
|---|---|---|---|---|---|
| Karta projektu, backlog i sprint review | A/R | C | C | C | C |
| Architektura logiczna i DFD | A/R | C | C | C | C |
| CI/CD SmartGate, GitHub Actions, security gates | C | A/R | R | R | I |
| Obraz OCI, GHCR, SBOM i Docker | C | R | A/R | C | I |
| VM Edge/Cloud, lokalna baza, sieć, deployment i rollback | C | R | A/R | C | I |
| Model zagrożeń STRIDE, IAM, ryzyka | C | C | C | A/R | C |
| Telemetria SmartGate/CI, dashboard i AI/ML | C | C | C | C | A/R |
| Integracja końcowa i demonstracja | A/R | R | R | R | R |

## Zasady współpracy

- Repozytorium: https://github.com/pniewrzol/-DevSecOps-Edge-Cloud-app
- Issues i Pull Requests jako historia zadań; każda zmiana powinna mieć review innej osoby.
- Decyzje techniczne i ryzyka dokumentowane po każdym przeglądzie sprintu.
- Materiały najlepiej udostępniać 48 godzin przed kolejnymi zajęciami.
- Bez sekretów i danych rzeczywistych w kodzie, logach i zrzutach.

## Dokumentowanie wkładu

Każdy członek zespołu przypisuje do swoich zadań link do issue, PR, commita lub dokumentu, który opracował.
