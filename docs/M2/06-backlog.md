# M2 – Backlog SmartGate

Właściciele poniżej odpowiadają za **następne prace** zgodnie z [planem ról](../M1/02-role-i-komunikacja.md). Faktyczny wkład do M2 jest zapisany w [rejestrze wkładu](../M1/02-role-i-komunikacja.md#wykonane-prace-m1-i-m2).

Na M2 gotowe są diagram, DFD, STRIDE, rejestr ryzyk i backlog. Działa lokalne API z testami oraz potok do publikacji obrazu. Szczegóły są w [dowodach M2](08-PoC-i-dowody.md).

| Etap | Zadanie | Planowany właściciel | Kiedy uznamy je za zrobione | Stan |
|---|---|---|---|---|
| M3 – 11.12 | Sprawdzić sieć Proxmox i CHR | Kamil | Obie VM mają Internet. Edge łączy się z Cloud po HTTPS. Cloud nie otwiera nowego połączenia do Edge. | Środowisko przygotowywane |
| M3 – 11.12 | Dostarczać dokładnie zeskanowany obraz | Michał | GHCR otrzymuje obraz z zadania skanowania. Digest jest zapisany do porównania przy wdrożeniu. | Do zrobienia |
| M3 – 11.12 | Uruchomić obraz na Edge | Kamil | Wdrożenie jest powtarzalne, API przechodzi healthcheck, a baza zostaje po restarcie. | Do zrobienia |
| M3 – 11.12 | Przesłać pierwszy raport do Cloud | Kamil | Odbiornik po HTTPS przyjmuje uwierzytelniony raport. Po przerwie Edge ponawia wysyłkę, a Cloud nie liczy duplikatu. | Do zrobienia |
| Po pierwszym przepływie M3 | Aktualizować abonamenty na Edge | Kamil | Edge przyjmuje tylko poprawne, uwierzytelnione i nowsze dane. | Do zrobienia |
| M4 – 12.12 | Wybrać wariant monitoringu i zebrać dane | Bartek | Dashboard pokazuje dane z Edge i GitHub Actions. Widać przynajmniej jeden alert. | Dwa warianty opisane |
| M4 – 12.12 | Ocenić analizę AI/ML | Bartek | Reguła i model mają wyniki precision, recall i F1 na tym samym oznaczonym zbiorze testowym. | Do zrobienia |
| M5 – 15.01 | Sprawdzić blokadę `CRITICAL` i działanie offline | Kajetan | Kontrolowany test zatrzymuje publikację. Edge odpowiada po utracie Cloud. Są wyniki i logi. | Do zrobienia |
| M5 – 15.01 | Sprawdzić rollback | Kamil | Po błędzie można wrócić do ostatniego poprawnego obrazu bez utraty bazy. Wynik jest zapisany. | Do zrobienia |
| M6 – 16.01 | Przejrzeć konfigurację i dowody | Kajetan | Można powiązać wydanie, skan, wdrożenie i rollback z logami. | Do zrobienia |
| M7 – 31.01 | Złożyć dokumentację i przygotować obronę | Patryk | Repozytorium, demonstracja i faktyczny wkład osób są udokumentowane. | Do zrobienia |

Daty M5–M7 dotyczą 2027 r. Kolejność prac zaczyna się od gotowego obrazu, sieci i jednego raportu. Dashboard i model mogą być przygotowywane równolegle na danych testowych.
