# Raport postępu przed M2 – SmartGate DevSecOps

**Stan na 22.11.2026**

Od M1 doprecyzowaliśmy przypadek użycia, podział odpowiedzialności i architekturę Edge–Cloud. Opracowaliśmy DFD, model zagrożeń STRIDE, rejestr ryzyk i backlog. Lokalny demonstrator rozpoznaje fikcyjne tablice na podstawie abonamentów z SQLite i zapisuje zdarzenia.

[Dowody M2](08-PoC-i-dowody.md) zawierają wyniki 10 testów, przykłady odpowiedzi API i odnośnik do zakończonego sukcesem przebiegu GitHub Actions. CI wykonało testy i skany, wygenerowało SBOM i opublikowało obraz w GHCR.

Następny krok to połączenie rozdzielonych środowisk Edge i Cloud oraz wdrażanie obrazu zweryfikowanego przez CI. W backlogu są także synchronizacja zdarzeń, kontrolowana blokada publikacji, rollback oraz monitoring i analiza telemetrii.
