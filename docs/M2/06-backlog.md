# M2-06. Backlog SmartGate DevSecOps – pięć osób, M2–M7

Statusy: `GOTOWA DOKUMENTACJA`, `ZWERYFIKOWANE`, `CZĘŚCIOWO`, `TODO`. P0 obowiązkowe; P1 ważne; P2 rozszerzenie. Dowodem wykonania zadania jest PR/commit, review i (gdy dotyczy) test/link do runu.

| ID | Etap | Zadanie | Właściciel | Priorytet | Kryterium akceptacji | Status |
|---|---|---|---|---|---|---|
| M2-01 | M2 27.11 | Karta projektu SmartGate, role i cel | Patryk | P0 | link, MVP parking + DevSecOps | GOTOWA DOKUMENTACJA |
| M2-02 | M2 | C4 / architektura Edge–Cloud | Patryk + Kamil | P0 | granice stref i komponenty | GOTOWA DOKUMENTACJA |
| M2-03 | M2 | DFD SmartGate + CI/CD | Patryk + Kajetan | P0 | dane, strefy, przepływy | GOTOWA DOKUMENTACJA |
| M2-04 | M2 | STRIDE i rejestr ryzyk | Kajetan | P0 | co najmniej 6 klas i testy | GOTOWA DOKUMENTACJA |
| M2-05 | M2 | Review ADR i decyzje otwarte | Patryk | P0 | status zaakceptowany przez zespół | TODO |
| M2-06 | M2 | PoC test/build/scan i dowody | Michał + Kajetan | P0 | zielone CI, raport skanów | ZWERYFIKOWANE ([#8](08-PoC-i-dowody.md)) |
| M2-07 | M2 | Symulator decyzji z fikcyjną tablicą | Kamil + Patryk | P1 | OPEN/DENY i 401, pytest | ZWERYFIKOWANE |
| M2-08 | M2 | Projekt danych i metryki AI | Bartek | P1 | baseline, schema, metryki | GOTOWA DOKUMENTACJA |
| M3-01 | M3 11.12 | Edge/Cloud – 2 VM lub logiczne strefy | Kamil + Michał | P0 | udokumentowana separacja | TODO |
| M3-02 | M3 | Lokalna SQLite abonamentów, outbox trwały | Kamil | P0 | offline decyzje i brak utraty zdarzeń | CZĘŚCIOWO: lokalny zapis zdarzeń |
| M3-03 | M3 | Synchronizacja raportu co 60 s i snapshot uprawnień | Kamil + Bartek | P0 | idempotencja, retry, auth/TLS | TODO |
| M3-04 | M3 | Zabezpieczenia API, polityka secretów | Kajetan | P0 | odmowa anonimowa, autoryzacja aktualizacji | CZĘŚCIOWO: demo API key |
| M3-05 | M3 | Publikacja zeskanowanego obrazu OCI i test blokady CRITICAL | Michał + Kajetan | P0 | publikacja obrazu o zweryfikowanym digescie; kontrolowana blokada publikacji | CZĘŚCIOWO: działa ścieżka pozytywna |
| M3-06 | M3 | Wdrożenie Edge/Cloud + healthcheck | Kamil + Michał | P0 | commit→CI→image→deploy | TODO |
| M3-07 | M3 | Rollback last-known-good + audyt | Kamil | P0 | wadliwa wersja automatycznie cofnięta | TODO |
| M4-01 | M4 12.12 | Telemetria z Edge i CI | Bartek | P0 | min. 2 źródła | TODO |
| M4-02 | M4 | Dashboard, alert zdarzeń parkingowych | Bartek | P0 | 1 wykryty incydent | TODO |
| M4-03 | M4 | Oznaczony dataset syntetyczny | Bartek | P0 | data split z opisem | TODO |
| M4-04 | M4 | Baseline i model ML | Bartek | P0 | precision/recall/F1 porównane | TODO |
| M5-01 | M5 15.01 | Plan i dowody testów (offline, API, CRITICAL) | Kajetan + Patryk | P0 | scenariusze i wyniki | TODO |
| M5-02 | M5 | Test rollbacku i odtwarzalności | Kamil | P0 | dowód odtworzenia | TODO |
| M6-01 | M6 16.01 | Audyt techniczny / przegląd konfiguracji | Kajetan + Patryk | P0 | lista kontroli i dowody | TODO |
| M7-01 | M7 31.01 | Finalny raport, repo, demo i wkład zespołu | Patryk + cały zespół | P0 | prezentacja end-to-end, Q&A | TODO |

**Ważne:** prace M3 i M4 trzeba prowadzić równolegle – odbiory dzieli jeden dzień. Patryk koordynuje review, ale właściciel danego zadania odpowiada za jego dowóz.
