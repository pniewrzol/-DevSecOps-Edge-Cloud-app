# Raport postępu przed M2

**25.11.2026**

Patryk przygotował kartę projektu, diagram Edge–Cloud, opis przepływu danych, model zagrożeń i backlog. Przygotował też lokalny demonstrator SmartGate oraz potok testów i publikacji.

SmartGate sprawdza fikcyjną tablicę w SQLite i zapisuje decyzję. Lokalnie przeszło 10 testów. W GitHub Actions przeszły testy i skany, powstał SBOM i opublikowano obraz w GHCR. [Wyniki i przebieg CI](08-PoC-i-dowody.md).

Przygotowano też dwie VM z Debianem i oddzielne sieci za MikroTik CHR. To baza pod próby wdrożenia.

Na M3 planujemy uruchomić sprawdzony obraz na VM Edge i pokazać pierwszy raport odebrany przez VM Cloud. Na M4 wybierzemy sposób monitoringu i sprawdzimy, czy metoda analizy wykrywa przygotowane przypadki anomalii. [Backlog](06-backlog.md) · [Plan monitoringu](10-plan-AI-ML.md).
