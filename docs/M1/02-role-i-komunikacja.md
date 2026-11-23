# M1 – Role, komunikacja i ślad wkładu (5 osób)

**Uzgodniony podział zespołu – projekt SmartGate DevSecOps:** Patryk – lider / architekt; Michał i Kamil – Cloud / DevOps; Kajetan – Security Engineer; Bartek – AI / Monitoring.

Prowadzący zaakceptował pięcioosobowy skład. Michał odpowiada za CI/CD, a Kamil za środowisko wdrożeniowe i synchronizację.

## Plan odpowiedzialności (RACI)

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

## Wykonane prace M1 i M2

Materiały M1 i M2 udostępnione w repozytorium opracował Patryk. Tabela obejmuje wykonane prace; plan odpowiedzialności jest opisany w macierzy powyżej.

| Etap | Osoba | Wykonana praca | Dowód |
|---|---|---|---|
| M1 | Patryk | Karta projektu, podział ról, plan sprintu i przygotowanie repozytorium | [Dokumentacja M1](01-karta-projektu.md), [historia repozytorium](https://github.com/pniewrzol/-DevSecOps-Edge-Cloud-app/commits/main/) |
| M2 | Patryk | Dokumentacja architektury, DFD, STRIDE i backlogu, kod i testy demonstratora, konfiguracja CI | [Przegląd M2](../M2/01-przeglad-M2.md), [przebieg CI #8](https://github.com/pniewrzol/-DevSecOps-Edge-Cloud-app/actions/runs/45068382402) |

Jeżeli ktoś wykonał pracę poza repozytorium, można dopisać osobny wiersz z etapem, nazwiskiem, konkretną czynnością i dowodem, np. notatką ze spotkania, recenzją projektu lub wynikiem testu.
