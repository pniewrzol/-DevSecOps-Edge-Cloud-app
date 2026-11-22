# M2-06. Backlog i harmonogram M2–M7

**Status początkowy:** `TODO` nie oznacza, że prace nie zostały rozpoczęte przez zespół; należy aktualizować faktyczny stan. Role wskazują właściciela merytorycznego; konkretne osoby: **[UZUPEŁNIĆ]**.

Priorytety: **P0** krytyczne do odbioru/MVP, **P1** ważne, **P2** rozszerzenie. Kryterium ukończenia zadania: artefakt w repo, review drugiej osoby, dowód testu (jeśli dotyczy), uaktualnione dokumenty.

| ID | Etap / termin | Zadanie (rezultat) | P | Rola | Kryterium akceptacji | Stan |
|---|---|---|---|---|---|---|
| M2-01 | M2 / 27.11.2026 | Weryfikacja karty M1 i ról | P0 | Lider | cel, MVP, 5 osób i role; potwierdzenie zgody prowadzącego | TODO |
| M2-00 | M2 | Potwierdzenie odstępstwa: zespół 5-osobowy | P0 | Lider | zgoda prowadzącego odnotowana w M1 | TODO |
| M2-02 | M2 | Diagram architektury i wykaz komponentów | P0 | Architekt | Edge, Cloud, CI, registry i monitoring na diagramie | TODO |
| M2-03 | M2 | DFD + granice zaufania | P0 | Architekt/Security | przepływy F01–F13, dane i transport | TODO |
| M2-04 | M2 | Model STRIDE | P0 | Security | min. 6 klas + kontrole i testy | TODO |
| M2-05 | M2 | Rejestr ryzyk | P0 | Security | 3 kluczowe ryzyka i mitigacje | TODO |
| M2-06 | M2 | Backlog, role, roadmap | P0 | Lider | zadania M2–M7, priorytety, kryteria | TODO |
| M2-07 | M2 | PoC newralgicznego elementu | P0 | DevOps | uruchomiony build+test+scan, dowody i link | TODO |
| M2-08 | M2 | Założenia metryk AI | P1 | AI | schema danych, baseline i miary | TODO |
| M3-01 | M3 / 11.12.2026 | VM Edge i Cloud odrębne logicznie | P0 | DevOps | diagram sieci i dostęp do obu hostów | TODO |
| M3-02 | M3 | Aplikacja kontenerowa i testy | P0 | DevOps | `/health` działa, testy green | TODO |
| M3-03 | M3 | Test, SAST, SCA, image scan | P0 | Security | blokada krytycznej podatności | TODO |
| M3-04 | M3 | GHCR + SBOM/manifest | P0 | DevOps | powtarzalna publikacja image digest + SBOM | TODO |
| M3-05 | M3 | Autoryzowany deployment Edge+Cloud | P0 | DevOps | pierwszy end-to-end oraz kontrola auth | TODO |
| M3-06 | M3 | Kontrole transmisji i uprawnień | P0 | Security | przegląd ACL/secretów/TLS/VPN | TODO |
| M3-07 | M3 | Rollback: wersja last-known-good | P0 | DevOps | przywrócenie po wadliwej aktualizacji | TODO |
| M4-01 | M4 / 12.12.2026 | Telemetria CI i Edge | P0 | AI | co najmniej dwa źródła w kolektorze | TODO |
| M4-02 | M4 | Dashboard i alert | P0 | AI | przykład incydentu widoczny w GUI | TODO |
| M4-03 | M4 | Dane syntetyczne z etykietami | P0 | AI | schema i podział train/test | TODO |
| M4-04 | M4 | Baseline regułowy | P0 | AI | wyniki bazowe na zbiorze testowym | TODO |
| M4-05 | M4 | Klasyfikator AI/ML | P0 | AI | precision/recall/F1, confusion matrix | TODO |
| M5-01 | M5 / 15.01.2027 | Plan testów i dowody | P0 | Security | scenariusze green, failed build/scan, rollback | TODO |
| M5-02 | M5 | Test autoryzacji i izolacji | P0 | Security | odmowa nieuprawnionego deploy/odczytu | TODO |
| M5-03 | M5 | Lista usterek i poprawek | P0 | Lider | priorytety, właściciele, status | TODO |
| M6-01 | M6 / 16.01.2027 | Odbiór prototypu | P0 | Zespół | działające demo na labie | TODO |
| M6-02 | M6 | Przegląd konfiguracji | P0 | Security | checklista kont, sekretów, sieci | TODO |
| M7-01 | M7 / 31.01.2027 | Repo finalne i instrukcja odtworzenia | P0 | Lider | czysty clone i uruchomienie | TODO |
| M7-02 | M7 | Raport, prezentacja i indywidualny wkład | P0 | Zespół | komplet dowodów, demo i Q&A | TODO |
| EXT-01 | opcjonalne | Rozbudowany Terraform/Ansible IaC | P2 | DevOps | idempotentne provisioning | TODO |
| EXT-02 | opcjonalne | Automatyczna reakcja na alert ML | P2 | AI | scenariusz, bez nadpisywania policy gate | TODO |

## Podział obowiązków dla 5 osób

- **Lider / Architekt:** karta M1, diagramy, backlog, koordynacja, repo i integracja.
- **DevOps / CI-CD:** GitHub Actions, skany w workflow, build, GHCR, SBOM, dowód PoC.
- **Security Engineer:** STRIDE, rejestr ryzyka, kontrola uprawnień, polityki skanowania.
- **Edge / Cloud Infrastructure Engineer:** strefy VM, komunikacja, runtime, deployment, rollback.
- **AI / Monitoring Engineer:** telemetria, schemat danych, baseline, klasyfikator i metryki jakości.

Nazwiska: [UZUPEŁNIĆ w `../M1/01-karta-projektu.md`]. Zgoda prowadzącego na pięć osób: [POTWIERDZIĆ].

## Zależności i krytyczna ścieżka

`M2-07 → M3-03 → M3-04 → M3-05 → M3-07 → M5-01 → M6-01`.

Równolegle: `M2-08 → M4-01 → M4-03 → M4-04 → M4-05`. Ponieważ M3 i M4 dzieli jeden dzień, rozwój danych i AI musi rozpocząć się wcześniej.

## Sprint review i praca zespołowa

- 48 h przed spotkaniem (zalecenie planu): oddać aktualne dokumenty i dowody.
- Każde zadanie ma issue, właściciela, PR, kryterium akceptacji.
- Każdy merge do `main` przechodzi review. Historia commitów pokazuje wkład indywidualny.
- Po review uaktualnić risk register, ADR, backlog i ograniczenia.
