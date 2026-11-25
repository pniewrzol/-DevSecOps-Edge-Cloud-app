# Infrastruktura Edge–Cloud

W obu wariantach SmartGate działa na Edge z lokalną bazą SQLite. Edge ma wysyłać zbiorcze raporty po HTTPS do Cloud. Usługa Cloud ma odbierać raporty i udostępniać dane do monitoringu.

## Wariant A – laboratorium na Proxmoxie

To wariant podstawowy. Dwie VM z Debianem działają na jednym hoście Proxmox, ale są w osobnych sieciach. MikroTik CHR łączy je z Internetem i kontroluje ruch między nimi.

| Element | Sieć lub zadanie |
|---|---|
| CHR `ether1` | WAN w obecnej sieci domowej przez `vmbr0` |
| Edge | `vmbr1`, sieć `10.77.10.0/24`, brama `10.77.10.1`. Uruchamia SmartGate i lokalną bazę. |
| Cloud | `vmbr2`, sieć `10.77.20.0/24`, brama `10.77.20.1`. Tu ma działać odbiornik raportów i monitoring. |

VM mogą wychodzić do Internetu. Edge inicjuje HTTPS do odbiornika na Cloud (`10.77.20.10:443`). Odpowiedzi wracają w ramach tego połączenia. Cloud nie inicjuje nowych połączeń do Edge. Zapora ma blokować obu VM dostęp do domowego LAN-u. [Diagram wariantu A](../docs/M2/02-architektura.md)

## Wariant B – lokalny Edge i Cloud na VPS

Jeśli prowadzący poprosi o środowisko poza Proxmoxem, Edge można uruchomić na osobnym komputerze z Debianem, a Cloud na maszynie wirtualnej wynajętej u dostawcy VPS.

| Element | Jak działa |
|---|---|
| Edge | Lokalny komputer z Debianem uruchamia obraz SmartGate z GHCR. Baza SQLite zostaje na tym komputerze. |
| Cloud | VPS z Debianem uruchamia odbiornik raportów i wybrany wariant monitoringu. Odbiornik ma nazwę DNS i certyfikat HTTPS. |
| Połączenie | Edge wysyła raport do odbiornika na VPS przez TCP 443. Operator konfiguruje adres odbiornika zamiast lokalnego `10.77.20.10`. |

Raport wysyłamy z kluczem odbiornika i bez numerów rejestracyjnych. Na VPS wystawiamy przez HTTPS ścieżkę do odbioru raportów. Panel administracyjny monitoringu zostaje dostępny przez tunel SSH, a dostęp administracyjny do VPS ograniczamy do uprawnionych osób. Edge rozpoczyna połączenie wychodzące, więc jego API może pozostać lokalne. Nie trzeba przekierowywać portów na domowym routerze. Ten wariant wymaga VPS i konfiguracji publicznego HTTPS.

## Co sprawdzimy na M3 w obu wariantach

1. Edge pobiera sprawdzony obraz z GHCR i uruchamia aplikację.
2. SmartGate zapisuje decyzję dla fikcyjnej tablicy, a Cloud odbiera zbiorczy raport po HTTPS.
3. Gdy Cloud jest niedostępny, Edge nadal podejmuje decyzje z lokalnej bazy.

[Backlog wdrożenia](../docs/M2/06-backlog.md) · [Warianty monitoringu](../docs/M2/10-plan-AI-ML.md)
