# Monitoring SmartGate

Chcemy sprawdzić, czy Edge wysyła raporty, jak często odmawia wjazdu i czy ostatnie wydanie przeszło przez CI. Monitoring działa po stronie Cloud. Poniżej są dwa warianty do wyboru na M4. Do demonstracji wystarczy wdrożyć jeden.

| Źródło | Co zbieramy |
|---|---|
| **SmartGate na Edge** | Czas odebrania ostatniego raportu, liczba decyzji `OPEN` i `DENY` w danym okresie oraz liczba zdarzeń czekających na wysłanie. |
| **GitHub Actions** | Czas i wynik przebiegu CI oraz wynik testów, skanów i publikacji obrazu, jeśli dany krok został uruchomiony. |

W obu wariantach Edge wysyła zbiorczy raport po HTTPS do Cloud. Cloud pobiera wyniki CI z API GitHuba. Dzięki temu Cloud nie musi inicjować połączenia do Edge. Raporty zawierają liczniki bez numerów rejestracyjnych. [Infrastruktura Edge–Cloud](../infrastructure/README.md)

## Wariant A – Prometheus i Grafana

Ten wariant daje gotowe wykresy i reguły alertów. Trzeba przygotować prostą usługę, która udostępni dane Prometheusowi.

| Element | Co robi |
|---|---|
| **Odbiornik raportów na Cloud** | Przyjmuje raporty Edge po HTTPS i udostępnia z nich metryki. |
| **Eksporter GitHub Actions** | Pobiera wyniki CI przez API GitHuba i udostępnia je jako metryki. |
| **Prometheus** | Regularnie odczytuje metryki od odbiornika i eksportera na Cloud, zapisując historię pomiarów. |
| **Grafana** | Pokazuje wykresy i tworzy alerty według ustalonych reguł. |
| **Skrypt analizy** | Ocenia okna danych za pomocą osobnego modelu, np. Isolation Forest. Wyniki porównujemy z prostą regułą. |

## Wariant B – Apache, n8n i OpenRouter

Ten wariant pozwala w jednym przepływie połączyć raporty Edge, dane GitHuba i analizę modelu. Trzeba przygotować prostą stronę z wynikami.

| Element | Co robi |
|---|---|
| **Apache** | Obsługuje HTTPS, przekazuje żądania z raportami do webhooka n8n i serwuje dashboard HTML oraz plik JSON z danymi. |
| **n8n** | Odbiera raporty przez uwierzytelniony webhook, pobiera wyniki CI, liczy wskaźniki i aktualizuje dane dashboardu. |
| **OpenRouter** | Daje dostęp do wybranego modelu chmurowego. Model dostaje statystyki i ocenia, czy dane okno wygląda na anomalię. |
| **Dashboard** | Pokazuje ostatni raport, udział odmów, status CI i listę alertów. |

Klucz OpenRouter zostaje w konfiguracji n8n. Model otrzymuje wyłącznie zagregowane dane. Dostęp do edytora n8n pozostaje administracyjny.

## Co sprawdzimy na M4 w obu wariantach

1. Dashboard pokazuje dane z obu źródeł: Edge i GitHub Actions.
2. Przygotowany przypadek anomalii pojawia się jako alert. Przykład to nagły wzrost odmów po nowym wydaniu.
3. Porównujemy model i prostą regułę na tych samych oznaczonych danych syntetycznych. Reguła może oznaczać anomalię przy ponad 70% odmów w 5 minut i co najmniej 20 zdarzeniach.
4. Zapisujemy wyniki precision, recall i F1. Gdy monitoring jest niedostępny, SmartGate nadal podejmuje decyzje na Edge na podstawie reguł i SQLite.

[Plan oceny analizy](../docs/M2/10-plan-AI-ML.md) · [Backlog M4](../docs/M2/06-backlog.md)
