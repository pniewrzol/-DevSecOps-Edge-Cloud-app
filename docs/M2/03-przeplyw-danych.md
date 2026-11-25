# M2 – Przepływ danych (DFD)

DFD pokazuje, jakie dane trafiają między klientem, aplikacją, magazynami i usługami. Strzałki przerywane dotyczą przyszłych prac.

```mermaid
flowchart TB
    U["Klient: fikcyjna tablica"]
    subgraph EDGE["Strefa Edge"]
        A["SmartGate: sprawdzenie tablicy"]
        D[("SQLite: abonamenty")]
        E[("SQLite: zdarzenia")]
        W["Plan: wysyłka raportów"]
        D -->|"F02: dane abonamentu"| A
        A -->|"F04: zapis zdarzenia"| E
    end
    subgraph CI["Strefa GitHub"]
        P["GitHub Actions"]
        R[("GHCR: obrazy")]
        S[("Actions: pliki SBOM")]
        P -->|"F06: obraz"| R
        P -->|"F07: SBOM"| S
    end
    subgraph CLOUD["Strefa Cloud"]
        O["Plan: odbiornik raportów"]
        H["Plan: pobieranie wyników CI"]
        T[("Wyniki i alerty")]
        O -.->|"F10: zapis wyników"| T
    end
    U -->|"F01: żądanie i klucz API"| A
    A -->|"F03: OPEN lub DENY"| U
    G["Repozytorium"] -->|"F05: kod do sprawdzenia"| P
    R -.->|"F08: pobranie obrazu"| A
    E -.->|"Zdarzenia do podsumowania"| W
    W -.->|"F09: zbiorczy raport HTTPS"| O
    P -.->|"F11: wyniki CI"| H
    H -.->|"Zapis wyników CI"| T
```

| Przepływ | Dane i stan |
|---|---|
| F01–F04 | Działają lokalnie. API przyjmuje fikcyjną tablicę, sprawdza abonament, zwraca wynik i zapisuje zdarzenie. |
| F05–F07 | Działają w CI. Obraz trafia do GHCR, a SBOM do artefaktów GitHub Actions. |
| F08 | Plan M3. Edge pobiera obraz do wdrożenia. |
| F09–F10 | Plan M3. Edge wysyła liczniki i identyfikator raportu po HTTPS. Cloud zapisuje raport raz, także po ponowieniu wysyłki. |
| F11 | Plan M4. Cloud pobiera wyniki CI jako drugie źródło monitoringu. |

`GET /api/v1/events/summary` już zwraca lokalne liczniki oraz liczbę zdarzeń oczekujących. Wysyłkę raportów trzeba jeszcze wdrożyć. W raportach do Cloud wystarczą zagregowane dane. Numery rejestracyjne pozostają lokalnie.
