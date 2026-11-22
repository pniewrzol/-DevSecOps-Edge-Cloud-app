# M2-07. Rejestr decyzji ADR – SmartGate

Status wskazuje, które decyzje są wdrożone w demonstratorze, a które wymagają uzgodnienia przed kolejnym etapem.

| ID | Status | Decyzja | Uzasadnienie / ryzyko |
|---|---|---|---|
| ADR-001 | UZGODNIONE W ZESPOLE | przypadek użycia SmartGate: lokalny szlaban parkingowy | czytelny scenariusz Edge–Cloud; bez fizycznego sprzętu |
| ADR-002 | WDROŻONE W DEMONSTRATORZE | FastAPI + SQLite na Edge | lokalne decyzje bez sieci, łatwe testy; ochrona bazy konieczna |
| ADR-003 | PROPONOWANE | dwie logicznie odrębne VM Edge i Cloud | spełnienie hybrydowości w Proxmox |
| ADR-004 | WDROŻONE W DEMONSTRATORZE | GitHub Actions + GHCR, hosted runner | izolacja CI, nie trzymać runnera na Edge |
| ADR-005 | WDROŻONE W DEMONSTRATORZE | SAST/SCA/Trivy, blokada CRITICAL, SBOM | powtarzalne security gates; skany nie zastępują review |
| ADR-006 | PROPONOWANE | lokalna kolejka SQLite + idempotentna synchronizacja co 60 sekund | zdarzenia nie giną offline; konieczne ID i retry |
| ADR-007 | DO DECYZJI | ważność snapshotu uprawnień w trybie offline | revocation versus dostępność; polityka fail-closed dla wygasłych uprawnień |
| ADR-008 | PROPONOWANE | osobna weryfikacja obrazów/digestu i rollback | kontrola integralności i odporności |
| ADR-009 | PROPONOWANE | AI/ML analizuje alarmy, nigdy nie otwiera szlabanu | rozdzielenie decyzji bezpieczeństwa od analityki |
| ADR-010 | WDROŻONE W DEMONSTRATORZE | dane wyłącznie fikcyjne, bez kamery ANPR i płatności | minimalizacja ryzyka, koncentracja na DevSecOps |
