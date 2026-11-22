# M2-10. Plan AI/ML i monitoringu SmartGate

**Cel:** wykrywanie nietypowych zdarzeń po wdrożeniu oraz problemów jakości CI/CD. **AI nie podejmuje decyzji `OPEN/DENY` ani nie obchodzi security gate.** W M2 jest to koncepcja, nie wytrenowany model.

## Dwa niezależne źródła telemetrii

1. **SmartGate Edge:** liczba decyzji OPEN/DENY/min, wskaźnik odmów, czas odpowiedzi, status lokalnej kolejki, zaległe raporty, dostępność Cloud, wersja aplikacji.
2. **GitHub Actions/DevSecOps:** status testów i skanów, CRITICAL/HIGH, czas budowania, SHA wersji, rollback.

## Proponowana analiza

- **Zdarzenie przykładowe:** po wydaniu nowej wersji skacze liczba odmów lub opóźnienie API; dodatkowo rośnie backlog raportów.
- **Baseline:** jawne reguły, np. >70% odmów w oknie 5 min i co najmniej 20 zdarzeń lub brak synchronizacji >180 s.
- **ML:** IsolationForest dla anomalii numerycznych albo nadzorowany klasyfikator (np. RandomForest) przy wystarczającym zbiorze oznaczonym.
- **Ocena:** precision, recall, F1 oraz false positive rate na odrębnym zbiorze testowym; porównać **te same** dane dla baseline i ML.
- **Dane:** wyłącznie syntetyczne, z oznaczeniem okien normalnych oraz incydentów; w metodologii podać seed, sposób generacji i podział, unikając przecieku danych między treningiem/testem.

## Oczekiwane dowody M4

| Dowód | Status |
|---|---|
| Telemetria Edge + CI z 2 źródeł | DO WYKONANIA |
| Jeden syntetyczny incydent i alert | DO WYKONANIA |
| Dataset train/test i opis etykiet | DO WYKONANIA |
| Wyniki baseline i ML (precision/recall/F1) | DO ZMIERZENIA |
| Dashboard lub raport wizualny | DO WYKONANIA |

**Ograniczenie:** mały sztuczny dataset może zawyżać wyniki modelu, co musi zostać omówione w raporcie.
