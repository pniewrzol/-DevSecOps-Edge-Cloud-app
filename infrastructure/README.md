# Infrastructure – SmartGate Edge–Cloud

W M3: osobna VM Edge z FastAPI, SQLite i trwałą kolejką zdarzeń, oddzielna VM Cloud z API raportowania i monitoringiem. Kanał VPN/HTTPS, uwierzytelnienie i segmentacja, brak publicznego Docker API. Weryfikować synchronizację co minutę, wersjonowane snapshoty abonamentów i rollback last-known-good. Na przeglądzie M2 pokazujemy lokalny demonstrator i publikację obrazu w GHCR.
