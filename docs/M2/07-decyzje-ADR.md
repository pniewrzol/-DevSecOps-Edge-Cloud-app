# M2-07. Dziennik decyzji architektonicznych (ADR)

Decyzje są **propozycjami**; zespół zaznacza `ZATWIERDZONE`, `ODRZUCONE` lub `DO DECYZJI` i wpisuje datę.

| ADR | Status | Decyzja | Uzasadnienie / kompromis |
|---|---|---|---|
| ADR-001 | DO DECYZJI | Dwie VM Edge + symulowana Cloud | spełnia hybrydowość bez płatnej chmury; trzeba utrzymywać VM |
| ADR-002 | DO DECYZJI | GitHub Actions + GHCR | proste CI i rejestr; ograniczenie zależnością od GitHub |
| ADR-003 | DO DECYZJI | FastAPI + Docker Compose | szybkie MVP; brak orkiestracji wielu hostów |
| ADR-004 | DO DECYZJI | Hosted runner dla PoC, zero self-hosted runner w Edge | dobra izolacja od labu; deploy wymaga osobnego bezpiecznego kanału |
| ADR-005 | DO DECYZJI | Blokada `CRITICAL` ze skanera Trivy | jednoznaczna reguła; możliwe false-positive i konieczne wyjątki |
| ADR-006 | DO DECYZJI | SBOM jako wymagany artefakt, Cosign dodatkowo | katalog akceptuje SBOM; podpis zwiększa pewność pochodzenia |
| ADR-007 | DO DECYZJI | Metryki z Edge i CI + ML do klasyfikacji alertów | spełnia 2 źródła i wymóg AI; potrzebne oznaczone syntetyczne dane |
| ADR-008 | DO DECYZJI | Deterministyczna blokada deploy, ML wyłącznie doradcze | brak automatycznych błędnych decyzji przez model |

## Szablon nowej decyzji

- ID i data:
- Kontekst i rozpatrzone warianty:
- Decyzja i właściciel:
- Konsekwencje i ryzyka:
- Test/warunek ponownego rozważenia:
