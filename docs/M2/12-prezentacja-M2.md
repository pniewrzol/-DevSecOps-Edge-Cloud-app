# M2-12. Scenariusz omówienia na spotkaniu

**Propozycja prezentacji około 7–10 minut; nie jest to limit narzucony przez prowadzącego.**

1. **1 min – Problem i MVP:** ryzyko manualnych wdrożeń, co system automatyzuje.
2. **2 min – Diagram:** GitHub/CI, GHCR, Edge, Cloud, monitoring; zaznaczyć granice zaufania.
3. **1–2 min – DFD:** przykład F01→F05→F07→F09; sekrety nigdy nie trafiają do kodu ani logów.
4. **2 min – STRIDE:** omówić T04, T07, T05 i zabezpieczenia/plan testów.
5. **1 min – Backlog:** najbliższe kamienie milowe M3 i M4 (tylko dzień odstępu).
6. **1–2 min – PoC:** pokazać prawdziwy run Actions i raport Trivy; jeśli brak runu, jawnie powiedzieć, że nie wykonano.

## Proponowany podział omówienia

- **Patryk:** cel, MVP, diagram i DFD.
- **Michał:** pipeline CI/CD, testy, publikacja GHCR.
- **Kamil:** Docker i plan infrastruktury Edge/Cloud, wdrożenie oraz rollback.
- **Kajetan:** model zagrożeń, ryzyka i kontrola bezpieczeństwa.
- **Bartek:** telemetria i metryki jakości AI/ML.

## Możliwe pytania prowadzącego

- **Co w projekcie jest hybrydowe?** Dwie logicznie odseparowane strefy Edge i Cloud oraz usługi SaaS CI.
- **Czy SBOM zapewnia integralność?** Nie; do integralności służą digesty/podpisy i kontrola dystrybucji artefaktów.
- **Co blokuje krytyczne CVE?** Twarda bramka skanera w CI przed push/deploy.
- **Jak unikniecie wycieku tokenu?** Least privilege, brak sekretów w PR, kontrola logów i repo.
- **Czy AI decyduje o wdrożeniu?** Nie. AI klasyfikuje alerty; security gate jest deterministyczny.
- **Jak działa rollback?** Po nieudanym healthcheck automatyczny powrót do ostatniego działającego digestu z audytem.
