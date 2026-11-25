# M2 – Decyzje projektowe

| Decyzja | Dlaczego | Stan |
|---|---|---|
| FastAPI i SQLite na Edge | API można szybko pokazać i przetestować. Lokalna baza pozwala podjąć decyzję przy braku Cloud. | Działa w demonstratorze |
| GitHub Actions, Semgrep, Trivy i GHCR | Wyniki testów, skanów i publikacji można prześledzić w jednym repozytorium. | Potwierdzone w CI |
| Oddzielne środowiska Edge i Cloud | Pozwalają pokazać granicę sieci i ograniczyć ruch do odbiornika HTTPS. | [Proxmox z CHR lub lokalny Edge i VPS](../../infrastructure/README.md) |
| Wysyłka liczników i ponawianie raportów | Cloud potrzebuje statystyk. Identyfikator pozwoli rozpoznać ponowienie. | Plan M3 |
| Prometheus + Grafana albo Apache + n8n + OpenRouter | Pierwsza opcja skupia się na metrykach i gotowych dashboardach. Druga na obiegu danych z API i klasyfikacji przez model chmurowy. | [Porównanie do decyzji](10-plan-AI-ML.md) |
| Decyzja `OPEN`/`DENY` na Edge | Aplikacja rozstrzyga na podstawie reguł i danych z SQLite. Analiza AI ma służyć alertom. | Decyzja lokalna działa |
