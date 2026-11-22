# M2-04. Model zagrożeń STRIDE

**Zakres analizy:** kod → CI → obraz OCI → Edge → monitoring/AI. **Metoda:** STRIDE na procesach, magazynach i przepływach DFD. Oceny wstępne i jakościowe; nie są wynikami pentestu.

## Aktywa i cele bezpieczeństwa

- A1: integralność repozytorium i workflow; A2: poświadczenia CI/CD; A3: integralność obrazu OCI i SBOM; A4: dostępność aplikacji Edge; A5: wiarygodność śladów audytowych; A6: prywatność i integralność danych telemetrii.

## Katalog zagrożeń

| ID | STRIDE | Zasób / przepływ | Scenariusz | Skutek | Kontrola | Test weryfikujący |
|---|---|---|---|---|---|---|
| T01 | S – Spoofing | GitHub/F01 | przejęcie konta autora | nieautoryzowane zmiany | MFA, branch protection, review | próbka PR bez aprobaty nie trafia na main |
| T02 | T – Tampering | CI/F02 | modyfikacja workflow lub wstrzyknięta akcja | obejście skanów | review workflow, pinning akcji SHA | zmiana workflow wymaga review |
| T03 | R – Repudiation | pipeline/F04 | brak możliwości ustalenia autora deploy | brak audytu | SHA, run ID, kto zatwierdził, timestamp | raport audit trail |
| T04 | I – Disclosure | sekrety/F06 | token w repo lub logach | kompromitacja deploymentu | Gitleaks, brak secretów na PR, maskowanie | kontrolowana próbka fałszywego sekretu |
| T05 | D – DoS | Edge/F08 | wadliwy obraz zatrzymuje usługę | niedostępność | healthcheck, rollback | wdrożenie celowo niesprawnej wersji |
| T06 | E – Elevation | runner CI | przejęcie runnera/roli | dostęp do registry/Edge | hosted izolowany runner, minimalne permissions, bez docker.sock | przegląd uprawnień workflow |
| T07 | T – Tampering | obraz/F05/F07 | podmiana obrazu | obcy kod na Edge | digest, podpis (jeśli wdrożony), SBOM | odmowa obrazu ze złym digestem |
| T08 | T – Tampering | SCA/build | zależność z krytyczną podatnością | znana ścieżka ataku | Trivy, fail pipeline CRITICAL | nieudany scan w odizolowanym teście |
| T09 | S – Spoofing | deploy/F06 | fałszywa dyspozycja deploy | nieautoryzowane wydanie | uwierzytelnienie, dostęp tylko main, approval | żądanie bez uprawnień jest odrzucone |
| T10 | I – Disclosure | telemetria/F09 | wyciek logów/endpointów | ekspozycja danych | VPN/TLS, auth, redakcja danych | endpoint niedostępny anonimowo |
| T11 | T – Tampering | AI/F10 | fałszywy wynik skanu | błędna klasyfikacja alertów | walidacja źródła/schema, identyfikacja runu | odrzucenie błędnych rekordów |
| T12 | D – DoS | monitoring/Cloud | przeciążenie telemetrią | utrata obserwowalności | limity, retencja, alert utraty scrape | symulacja niedostępności źródła |

Legenda: S = podszywanie, T = modyfikacja, R = zaprzeczalność, I = ujawnienie informacji, D = odmowa usługi, E = eskalacja uprawnień.

## Scenariusz incydentu do demonstracji

**INC-01: blokada krytycznej podatności**: w kontrolowanym przebiegu dostarczany jest artefakt z wynikami skanu `CRITICAL`. Pipeline powinien zakończyć się niepowodzeniem, zapisać raport i nie uruchomić etapu publikacji/wdrożenia. Próbki testowe wyłącznie w odizolowanym laboratorium.

**INC-02: wadliwa aktualizacja i rollback**: poprawnie zbudowana wersja z niespełnionym healthcheck ma spowodować powrót do poprzedniego działającego digestu, z logiem zdarzenia.

## Ryzyka rezydualne / ograniczenia

- SAST/SCA nie wykrywają wszystkich luk; brak CVE ≠ brak podatności.
- Pojedyncza VM Edge nie gwarantuje HA; rollback usuwa wybrane awarie wdrożenia, nie awarie fizyczne hosta.
- SBOM zapewnia identyfikację składników, ale samodzielnie nie uwierzytelnia obrazu.
- Klasyfikator ML nie może samodzielnie zatwierdzać wdrożenia; polityki deterministyczne mają pierwszeństwo.
