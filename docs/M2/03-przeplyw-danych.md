# M2-03. DFD – przepływy danych SmartGate

**Notacja:** E – encja zewnętrzna, P – proces, D – magazyn, TB – granica zaufania. Kierunki transportu są logiczne i nie oznaczają wdrożonych połączeń.

```mermaid
flowchart LR
  E1["E1 Klient HTTP"] -->|F01 fikcyjny numer| P1
  subgraph TB2["TB2 Edge"]
    P1["P1 Walidacja i autoryzacja klienta"] -->|F02 numer| P2["P2 Decyzja parkingowa"]
    D1[("D1 SQLite – abonamenty")] -->|F03 uprawnienia| P2
    P2 -->|F04 OPEN/DENY| E2["E2 Symulator szlabanu"]
    P2 -->|F05 zdarzenie| D2[("D2 Offline event outbox")]
    D2 -->|F06 zdarzenia do wysłania| P3["P3 Agent synchronizacji"]
    P3 -->|F08b zapis zweryfikowanej listy| D1
    P8["P8 Agent wdrożeniowy Edge"] -->|F12 aktualizacja i healthcheck| P1
  end
  subgraph TB3["TB3 Cloud"]
    P4["P4 Odbiór raportów"] --> D3[("D3 Raporty i historia")]
    P5["P5 Zarządzanie abonamentami"] -->|F08a wersjonowany snapshot| P3
    D3 --> P6["P6 Monitoring i AI/ML"]
  end
  P3 -->|F07 raport HTTPS/VPN| P4
  subgraph TB1["TB1 CI i Registry"]
    E3["E3 Programista"] -->|F09 kod PR| P7["P7 CI: test + SAST/SCA + build"]
    P7 -->|F10a obraz| D4[("D4 GHCR")]
    P7 -->|F10b SBOM| D5[("D5 Artefakty GitHub Actions")]
  end
  D4 -->|F11 obraz do deploy| P8
  P7 -->|F13 wyniki i zdarzenia CI| P6
```

| ID | Informacja i cel | Kontrola |
|---|---|---|
| F01 | Fikcyjna tablica do Edge | walidacja formatu, ograniczenie źródeł |
| F02–F03 | tablica i lokalne abonamenty | autoryzowany dostęp, ochrona SQLite |
| F04 | decyzja OPEN/DENY do symulatora | odseparowane sterowanie (bez sprzętu) |
| F05–F06 | lokalne zdarzenia do trwałej kolejki | identyfikator i czas, brak utraty po restarcie |
| F07 | zbuforowane raporty do Cloud | TLS/VPN, retry i idempotencja |
| F08a–F08b | wersjonowana lista abonamentów do Edge | autoryzacja, integralność, kontrola wieku danych |
| F09 | PR i kod źródłowy do CI | review, brak sekretów w PR |
| F10a–F10b | obraz do GHCR i SBOM do artefaktów Actions | publikacja po przejściu bramek CI; identyfikacja obrazu przez digest |
| F11–F12 | wdrożenie Edge i healthcheck | kanał uwierzytelniony, rollback |
| F13 | wyniki pipeline do Cloud | bez sekretów, ograniczona telemetria |

**Stan M2:** F01–F05 działają lokalnie przez API i SQLite. F09 i F10a–F10b działają w GitHub Actions. Synchronizacja z Cloud, wdrożenie na Edge i eksport telemetrii pozostają w planie.
