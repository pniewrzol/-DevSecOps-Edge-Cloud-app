# Laboratorium Edge–Cloud

Proxmox zapewnia dwie VM z Debianem. MikroTik CHR łączy ich sieci z Internetem i kontroluje ruch między nimi.

| Element | Sieć lub zadanie |
|---|---|
| CHR `ether1` | WAN w obecnej sieci domowej przez `vmbr0` |
| Edge | `vmbr1`, podsieć `10.77.10.0/24`, brama `10.77.10.1`. Tu działa SmartGate z lokalną bazą. |
| Cloud | `vmbr2`, podsieć `10.77.20.0/24`, brama `10.77.20.1`. Tu ma działać odbiornik raportów i monitoring. |

VM mogą wychodzić do Internetu. Między strefami Edge inicjuje HTTPS do odbiornika na Cloud (`10.77.20.10:443`). Odpowiedzi wracają w ramach tego połączenia. Cloud nie inicjuje nowych połączeń do Edge. Dostęp do domowego LAN-u ma pozostać zablokowany dla obu VM.

Na M3 trzeba potwierdzić reguły, pobrać właściwy obraz, uruchomić go na Edge i pokazać raport odebrany na Cloud. [Diagram](../docs/M2/02-architektura.md) · [Backlog](../docs/M2/06-backlog.md).
