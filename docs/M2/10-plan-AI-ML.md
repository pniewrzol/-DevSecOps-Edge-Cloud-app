# M2-10. Plan komponentu AI/ML i monitoringu

**Cel:** klasyfikacja alarmów CI/CD na `routine`, `security`, `quality`, `deployment_failure` oraz sygnalizowanie zdarzeń wymagających reakcji. Model nie steruje polityką publikacji — blokady CI są deterministyczne.

## Źródła danych (minimum dwa)

1. GitHub Actions / skanery – `pipeline_result`, `tests_failed`, `critical_cves`, `high_cves`, `build_duration_seconds`.
2. Edge / Prometheus – `healthcheck_ok`, `http_5xx_rate`, `deployment_duration`, `rollback_required`.

## Dane

W M4: oznaczony, syntetyczny zbiór o klasach normal/security/quality/deployment_failure. Podać liczbę próbek, sposób generacji, udział klas i ograniczenia. Separować trening i test; nie wykorzystywać tego samego przebiegu zdarzenia po obu stronach podziału.

## Metody

- Baseline: ręczne reguły, np. `critical_cves > 0 → security`, `tests_failed > 0 → quality`, `healthcheck_ok=0 → deployment_failure`.
- ML: prosty `DecisionTreeClassifier` albo `RandomForestClassifier` z `scikit-learn`.
- Miary: `precision`, `recall`, `macro-F1`, macierz pomyłek, liczba false positives; zestawić baseline i ML na tym samym teście.
- Monitorować opóźnienie klasyfikacji i wolumen zdarzeń, jeśli dane pozwolą.

## Uzasadnienie

Pipeline generuje sygnały z różnych etapów; klasyfikator może nadać alertom wspólną kategorię oraz priorytet dla operatora. Na małych danych syntetycznych możliwe jest zawyżenie jakości — koniecznie pokazać ograniczenia i bazowe reguły.

## Wyniki do uzupełnienia przy M4

| Parametr | Baseline | ML |
|---|---|---|
| Liczba próbek testowych | [DO ZMIERZENIA] | [DO ZMIERZENIA] |
| Precision (macro) | [DO ZMIERZENIA] | [DO ZMIERZENIA] |
| Recall (macro) | [DO ZMIERZENIA] | [DO ZMIERZENIA] |
| F1 (macro) | [DO ZMIERZENIA] | [DO ZMIERZENIA] |
| False positives | [DO ZMIERZENIA] | [DO ZMIERZENIA] |
