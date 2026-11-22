# M2-12. Prezentacja SmartGate DevSecOps (propozycja 7–10 min)

1. **Patryk (1–2 min):** cel tematu 04, przykład szlabanu, zakres MVP vs plan M3–M4, diagram Edge–Cloud.
2. **Kamil (1 min):** lokalna decyzja SQLite, tryb offline i plan synchronizacji / rollbacku.
3. **Michał (2 min):** GitHub Actions, pytest, skanery, GHCR, co już działa i co należy naprawić.
4. **Kajetan (1–2 min):** STRIDE – fałszywy klient, modyfikacja abonamentów, podatny obraz, zabezpieczenia.
5. **Bartek (1 min):** dwa źródła telemetrii, anomalie, baseline i metryka F1.
6. **Patryk (1 min):** podsumowanie, backlog, termin następnego etapu.

## Demo

- Pokazać `/health` i `/docs` na porcie 8003.
- Sprawdzić fikcyjną tablicę `SK 12345` → `OPEN`, `KR 98765` → `DENY`.
- Sprawdzić brak API key → `401`.
- Pokazać prawdziwy GitHub Actions i odróżnić zrealizowane kontrole od planowanych.

## Pytania

**Czy to jest tylko projekt szlabanu?** Nie. Szlaban to przypadek użycia do weryfikacji DevSecOps, bezpieczeństwa dostaw i Edge–Cloud.

**Czy system działa offline?** Lokalna baza obsługuje decyzję, ale symulacja awarii i synchronizacji kolejki wymaga implementacji M3.

**Czy AI otwiera bramę?** Nie. Decyzja jest deterministyczna, AI klasyfikuje alarmy i anomalie.

**Czy SBOM zabezpiecza integralność?** Sam SBOM nie; stosuje się digest i ewentualny podpis.
