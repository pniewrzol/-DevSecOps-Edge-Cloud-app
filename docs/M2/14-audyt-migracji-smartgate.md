# M2-14. Audyt GitHub i migracja do SmartGate

**Repozytorium źródłowe:** `pniewrzol/-DevSecOps-Edge-Cloud-app`, zweryfikowany stan gałęzi main: `0c52d7dd7284d80f7cae268d2a0dcd4802f276bd` (22.11.2026). Zaktualizowana paczka została oparta na pełnej kopii tych plików; brak zapisu bezpośrednio do GitHub z powodu 403 uprawnień integracji.

## Ustalenia audytu

| Wniosek | Istotność | Zmiana |
|---|---|---|
| Dokumentacja opisuje ogólną aplikację, nie SmartGate | wysoka | wymieniono kartę, C4, DFD, STRIDE, ADR, ryzyka, backlog, AI, matrycę i demo |
| Pipeline Actions run 45059847478 zakończył się błędem `Tests` | wysoka | `pytest -q` → `python -m pytest -q`; dokładna przyczyna wymaga logu; przebieg CI do powtórzenia |
| Brak API kontroli szlabanu | wysoka | dodano lokalny symulator decyzji SQLite, fikcyjne tablice i testy |
| Brak rzeczywistego Cloud sync i rollback | wysoka | pozostawiono jako plan M3–M5, bez fałszywych deklaracji |
| Historyczne 2/2 PASS dotyczą poprzedniej aplikacji | wysoka | zachowano protokół bez przypisywania wyników nowej logice |
| Publiczne API bez auth dla logiki parkingu | średnia | wprowadzono demonstracyjny wymagany nagłówek X-API-Key; docelowe IAM nadal planowane |
| Docker w read-only potrzebuje trwałego miejsca na SQLite | średnia | nazwany wolumin Docker `/data`, użytkownik non-root |
| W rejestrze ryzyk był błędny zwrot `Kajetan Engineer` | niska | zastąpiono poprawnym opisem właścicieli |
| Port w konfiguracji i lokalnym skrypcie | zgodność | zachowano 8003 |
| Repo zawiera źródłowe PDF | bez zmian | zachowano oryginalne pliki |

## Pozostałe zadania

1. Uruchomić nowy zestaw testów i sprawdzić build kontenera w środowisku zespołu; dołączyć logi.
2. Zweryfikować Semgrep i Trivy, brak krytycznych podatności oraz generowanie SBOM w GitHub Actions.
3. Ustalić politykę ważności abonamentów przy braku łączności.
4. Zaprojektować i przetestować autoryzowaną synchronizację, idempotencję i trwałość zdarzeń.
5. Wykonać audyt sekretów, odporności i wdrożenia Edge na M3–M5.

**Nie wdrażać tego demonstratora do prawdziwego szlabanu ani nie używać prawdziwych numerów rejestracyjnych.**
