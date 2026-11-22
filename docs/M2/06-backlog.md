# M2-06. Backlog i harmonogram M2–M7

**Status początkowy:** `TODO` nie oznacza, że prace nie zostały rozpoczęte przez zespół; należy aktualizować faktyczny stan. Role i osoby zostały przypisane zgodnie z uzgodnionym składem pięcioosobowym. Michał i Kamil współdzielą rolę Cloud / DevOps.

Priorytety: **P0** krytyczne do odbioru/MVP, **P1** ważne, **P2** rozszerzenie. Kryterium ukończenia zadania: artefakt w repo, review drugiej osoby, dowód testu (jeśli dotyczy), uaktualnione dokumenty.

| ID | Etap / termin | Zadanie (rezultat) | P | Rola | Kryterium akceptacji | Stan |
|---|---|---|---|---|---|---|
| M2-01 | M2 / 27.11.2026 | Weryfikacja karty M1 i ról | P0 | Patryk | cel, MVP, 5 osób i role; potwierdzenie zgody prowadzącego | TODO |
| M2-00 | M2 | Potwierdzenie odstępstwa: zespół 5-osobowy | P0 | Patryk | zgoda prowadzącego odnotowana w M1 | TODO |
| M2-02 | M2 | Diagram architektury i wykaz komponentów | P0 | Patryk | Edge, Cloud, CI, registry i monitoring na diagramie | TODO |
| M2-03 | M2 | DFD + granice zaufania | P0 | Patryk / Kajetan | przepływy F01–F13, dane i transport | TODO |
| M2-04 | M2 | Model STRIDE | P0 | Kajetan | min. 6 klas + kontrole i testy | TODO |
| M2-05 | M2 | Rejestr ryzyk | P0 | Kajetan | 3 kluczowe ryzyka i mitigacje | TODO |
| M2-06 | M2 | Backlog, role, roadmap | P0 | Patryk | zadania M2–M7, priorytety, kryteria | TODO |
| M2-07 | M2 | PoC newralgicznego elementu | P0 | Michał (wsparcie Kamil) | uruchomiony build+test+scan, dowody i link | TODO |
| M2-08 | M2 | Założenia metryk AI | P1 | Bartek | schema danych, baseline i miary | TODO |
| M3-01 | M3 / 11.12.2026 | VM Edge i Cloud odrębne logicznie | P0 | Kamil (wsparcie Michał) | diagram sieci i dostęp do obu hostów | TODO |
| M3-02 | M3 | Aplikacja kontenerowa i testy | P0 | Kamil (wsparcie Michał) | `/health` działa, testy green | CZĘŚCIOWO: lokalne 2/2 PASS 22.11, kontener do weryfikacji |
| M3-03 | M3 | Test, SAST, SCA, image scan | P0 | Kajetan (wsparcie Michał) | blokada krytycznej podatności | TODO |
| M3-04 | M3 | GHCR + SBOM/manifest | P0 | Michał (wsparcie Kamil) | powtarzalna publikacja image digest + SBOM | TODO |
| M3-05 | M3 | Autoryzowany deployment Edge+Cloud | P0 | Kamil (wsparcie Michał) | pierwszy end-to-end oraz kontrola auth | TODO |
| M3-06 | M3 | Kontrole transmisji i uprawnień | P0 | Kajetan (wsparcie Kamil) | przegląd ACL/secretów/TLS/VPN | TODO |
| M3-07 | M3 | Rollback: wersja last-known-good | P0 | Kamil (wsparcie Michał) | przywrócenie po wadliwej aktualizacji | TODO |
| M4-01 | M4 / 12.12.2026 | Telemetria CI i Edge | P0 | Bartek | co najmniej dwa źródła w kolektorze | TODO |
| M4-02 | M4 | Dashboard i alert | P0 | Bartek | przykład incydentu widoczny w GUI | TODO |
| M4-03 | M4 | Dane syntetyczne z etykietami | P0 | Bartek | schema i podział train/test | TODO |
| M4-04 | M4 | Baseline regułowy | P0 | Bartek | wyniki bazowe na zbiorze testowym | TODO |
| M4-05 | M4 | Klasyfikator AI/ML | P0 | Bartek | precision/recall/F1, confusion matrix | TODO |
| M5-01 | M5 / 15.01.2027 | Plan testów i dowody | P0 | Kajetan | scenariusze green, failed build/scan, rollback | TODO |
| M5-02 | M5 | Test autoryzacji i izolacji | P0 | Kajetan | odmowa nieuprawnionego deploy/odczytu | TODO |
| M5-03 | M5 | Lista usterek i poprawek | P0 | Patryk | priorytety, właściciele, status | TODO |
| M6-01 | M6 / 16.01.2027 | Odbiór prototypu | P0 | Cały zespół | działające demo na labie | TODO |
| M6-02 | M6 | Przegląd konfiguracji | P0 | Kajetan | checklista kont, sekretów, sieci | TODO |
| M7-01 | M7 / 31.01.2027 | Repo finalne i instrukcja odtworzenia | P0 | Patryk | czysty clone i uruchomienie | TODO |
| M7-02 | M7 | Raport, prezentacja i indywidualny wkład | P0 | Cały zespół | komplet dowodów, demo i Q&A | TODO |
| EXT-01 | opcjonalne | Rozbudowany Terraform/Ansible IaC | P2 | Michał / Kamil | idempotentne provisioning | TODO |
| EXT-02 | opcjonalne | Automatyczna reakcja na alert ML | P2 | Bartek | scenariusz, bez nadpisywania policy gate | TODO |

## Podział obowiązków dla 5 osób

- **Patryk – Lider / architekt:** karta M1, diagramy, DFD, backlog, koordynacja, integracja i przeglądy.
- **Michał – Cloud / DevOps:** CI/CD, GitHub Actions, skany w workflow, publikacja GHCR, proces release; współpraca z Kamilem.
- **Kamil – Cloud / DevOps:** Docker, konfiguracja VM Edge/Cloud, sieć, wdrożenia, healthcheck i rollback; współpraca z Michałem.
- **Kajetan – Security Engineer:** STRIDE, rejestr ryzyka, IAM, polityki bezpieczeństwa, skany i scenariusze testów.
- **Bartek – AI / Monitoring:** telemetria z CI i Edge, dashboard, alerty, baseline ML, klasyfikator i raport jakości.

**Uzgodnione przez zespół; zgoda prowadzącego na 5 osób: [POTWIERDZIĆ].**

## Zależności i krytyczna ścieżka

`M2-07 → M3-03 → M3-04 → M3-05 → M3-07 → M5-01 → M6-01`.

Równolegle: `M2-08 → M4-01 → M4-03 → M4-04 → M4-05`. Ponieważ M3 i M4 dzieli jeden dzień, rozwój danych i AI musi rozpocząć się wcześniej.

## Sprint review i praca zespołowa

- 48 h przed spotkaniem (zalecenie planu): oddać aktualne dokumenty i dowody.
- Każde zadanie ma issue, właściciela, PR, kryterium akceptacji.
- Każdy merge do `main` przechodzi review. Historia commitów pokazuje wkład indywidualny.
- Po review uaktualnić risk register, ADR, backlog i ograniczenia.
