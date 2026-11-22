# M3 – infrastruktura (miejsce na implementację)

W M2 brak konfiguracji produkcyjnego deploymentu. Zadania M3:

- `edge-01` i `cloud-01`: dwie logicznie oddzielone VM/segmenty.
- Kanał zaufania dla deploy oraz telemetrii (VPN/TLS, uwierzytelnienie, least privilege).
- Przypięcie wydania do digestu SHA256 i zapis ostatniej działającej wersji.
- Healthcheck i rollback; pełna demonstracja i zapis wyników.

Nie kopiować na serwer prywatnych kluczy ani nie publikować tokenów w repo.
