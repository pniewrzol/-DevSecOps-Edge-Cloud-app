# M2-04. Model zagrożeń STRIDE – SmartGate DevSecOps

Analiza dotyczy zarówno aplikacji parkingowej, jak i łańcucha dostaw CI/CD. Testy potwierdzają odmowę bez klucza. Kontrole Cloud i wdrożenia opisują projekt docelowy.

## Aktywa

A1 integralność lokalnych uprawnień abonamentowych; A2 poprawność decyzji `OPEN/DENY`; A3 dostępność Edge offline; A4 prywatność danych parkingowych; A5 integralność zdarzeń i raportów; A6 bezpieczeństwo pipeline i publikowanych artefaktów; A7 sekrety API i kont technicznych.

| ID | STRIDE | Scenariusz / granica | Skutek | Kontrola | Dowód/test |
|---|---|---|---|---|---|
| SG-01 | Spoofing | klient podszywa się pod zaufany odczyt tablicy | nieuprawnione żądania | API key demo; docelowo mTLS i identyfikacja urządzeń | 401 bez klucza |
| SG-02 | Tampering | zmiana uprawnienia w lokalnej SQLite | nieautoryzowane OPEN | ACL hosta, ograniczenie edycji, integralność snapshotów | test modyfikacji offline |
| SG-03 | Repudiation | usunięcie historii wjazdów | brak audytu | trwałe zdarzenia i centralna kopia | audyt/identyfikatory |
| SG-04 | Information Disclosure | ujawnienie tablic / abonamentów | naruszenie prywatności | tylko fikcyjne dane, TLS, retencja, RBAC | test anonimizacji |
| SG-05 | Denial of Service | nadmiar żądań parkingowych lub Cloud offline | spadek dostępności | rate limit, lokalna baza, kolejka | test offline i przeciążenia |
| SG-06 | Elevation of Privilege | podniesienie praw API do edycji abonamentów | fałszywy dostęp | brak publicznego endpointu admin, RBAC w Cloud | odmowa nieuprawnionej zmiany |
| SG-07 | Spoofing | fałszywy raport Edge w centrali | fałszywe statystyki | podpis/identyfikacja urządzenia, nonce/ID | odrzucenie obcego urządzenia |
| SG-08 | Tampering | ponowienie lub zmiana raportu | zawyżenie liczby wjazdów | event UUID, idempotencja | powtórny raport liczony raz |
| SG-09 | Tampering | cofnięcie wersji abonamentów | cofnięty zakaz wjazdu | wersja monotoniczna + termin ważności | odrzucenie starego snapshotu |
| CI-01 | Spoofing | przejęte konto GitHub lub nieuprawniony PR | kod obcy w release | MFA, branch protection, review | test reguł PR |
| CI-02 | Information Disclosure | sekret w repo lub logu Actions | przejęcie usługi | secrets manager, Gitleaks, brak sekretów w PR | test kontrolny |
| CI-03 | Tampering | niezweryfikowany obraz OCI | złośliwa aplikacja na Edge | Trivy, digest, SBOM i opcjonalny Cosign | blokada CRITICAL |
| CI-04 | Elevation of Privilege | runner uzyskuje dostęp do hosta Edge | przejęcie hosta | hosted isolated runner, least privilege | audyt workflow |
| CI-05 | Denial of Service | wadliwy deploy | brak usługi | healthcheck i rollback | test przywrócenia |

## Scenariusze weryfikacji

1. **Niedozwolony dostęp:** wywołanie `/api/v1/access/check` bez API key kończy się `401` (zabezpieczenie demonstracyjne, nie produkcyjne IAM).
2. **Blokada CRITICAL:** w kontrolowanym teście sprawdzić, czy bramka Trivy kończy zadanie błędem i blokuje publikację (do wykonania).
3. **Uszkodzona wersja:** nieudany healthcheck powoduje rollback z audytem (do wykonania M3–M5).
4. **Offline:** Edge podejmuje lokalne decyzje i przechowuje raporty do wznowienia łączności (plan testów M3–M5).

**Ograniczenia:** znana tablica nie dowodzi tożsamości pojazdu, skany nie gwarantują braku luk, API key demo bez rotacji nie wystarcza do wdrożenia produkcyjnego, a SBOM nie jest podpisem integralności.
