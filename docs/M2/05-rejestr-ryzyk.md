# M2-05. Rejestr ryzyk

Skala: **P** prawdopodobieństwo 1–3, **I** wpływ 1–3, **R=P×I** (1–2 niskie; 3–4 średnie; 6–9 wysokie). Oceny szacunkowe przed testami. Właścicieli przypisano według uzgodnionego podziału ról. Oceny ryzyka nadal są szacunkowe.

| ID | Ryzyko | P | I | R | Priorytet | Działanie | Właściciel roli | Dowód skuteczności |
|---|---|---:|---:|---:|---|---|---|---|
| R01 | Wyciek sekretów/tokenu | 2 | 3 | 6 | wysokie | Gitleaks, brak sekretów w repo, uprawnienia minimalne | Kajetan | test i przegląd ustawień CI |
| R02 | Podatny lub podmieniony obraz | 2 | 3 | 6 | wysokie | SCA, skan obrazu, digest, SBOM | Michał / Kajetan | zablokowany skan, raport |
| R03 | Niedostępność Edge po deploy | 2 | 3 | 6 | wysokie | healthcheck, wersja last-known-good, rollback | Kamil | demonstracja awarii i odtworzenia |
| R04 | Escalation z CI do Edge | 2 | 3 | 6 | wysokie | runner izolowany, oddzielny agent/poświadczenie | Kajetan | przegląd ról i uprawnień |
| R05 | Niepowodzenie integracji Edge–Cloud | 2 | 2 | 4 | średnie | test sieci, TLS/VPN, wczesny end-to-end | Patryk | odbiór M3 |
| R06 | Niewiarygodna metryka AI | 2 | 2 | 4 | średnie | train/test split, baseline, F1, confusion matrix | Bartek | raport M4 |
| R07 | Zbyt szeroki zakres / mało czasu | 3 | 2 | 6 | wysokie | MVP first, etapowanie i WIP limit | Patryk | aktualny backlog |
| R08 | Ujawnienie logów | 2 | 2 | 4 | średnie | kontrola dostępu, retencja, redakcja | Bartek / Kajetan | test odmowy dostępu |

## Procedura aktualizacji

Na każdym spotkaniu: przegląd ocen, oznaczenie nowych ryzyk, przypisanie osoby, zarejestrowanie decyzji i odnośnika do testu. Akceptację ryzyka wysokiego zatwierdza lider wraz z Kajetan Engineer.
