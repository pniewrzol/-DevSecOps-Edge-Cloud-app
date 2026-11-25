# M2 – Rejestr ryzyk

Oceniamy prawdopodobieństwo (P) i wpływ (W) od 1 do 3. Wynik to P × W. Zaczynamy od najwyższych wyników. Właściciel oznacza osobę odpowiedzialną według [planu ról](../M1/02-role-i-komunikacja.md).

| ID | Ryzyko | P | W | Wynik | Co robimy | Właściciel |
|---|---|---:|---:|---:|---|---|
| R1 | Nieuprawniona zmiana abonamentu daje fałszywe `OPEN`. | 2 | 3 | 6 | Ograniczamy dostęp do SQLite. Sprawdzamy ważność abonamentu i walidujemy aktualizacje. | Kajetan |
| R2 | Na Edge trafia podatny lub podmieniony obraz. | 2 | 3 | 6 | Skanujemy obraz. Planujemy publikację dokładnie zeskanowanego obrazu oraz weryfikację digestu przy wdrożeniu. | Michał |
| R3 | Awaria sieci lub wdrożenia przerywa działanie i wysyłanie raportów. | 3 | 3 | 9 | Decyzje podejmujemy lokalnie. Planujemy ponowienia, healthcheck i rollback. | Kamil |
| R4 | Klucz API lub token trafia do logów. | 2 | 3 | 6 | Trzymamy klucze poza kodem i ograniczamy uprawnienia. Przeglądamy logi przed pokazem. | Kajetan |
| R5 | Model daje za dużo fałszywych alertów. | 2 | 2 | 4 | Porównujemy go z prostą regułą na tych samych przypadkach testowych. | Bartek |

R1–R3 to trzy ryzyka z [karty M1](../M1/01-karta-projektu.md). Sprawdzamy je ponownie przed wdrożeniem.
