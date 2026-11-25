# M2 – Dwa warianty monitoringu i analizy

Chcemy widzieć, czy Edge odpowiada, dostarcza raporty i jak często odmawia wjazdu. Drugim źródłem są wyniki GitHub Actions, np. wynik testów, skanów i czas przebiegu. Na M2 projektujemy rozwiązanie. Wdrożenie monitoringu i ocena algorytmu są zadaniami M4.

| Wariant | Jak działa | Co trzeba przygotować |
|---|---|---|
| **A. Prometheus + Grafana** | Prometheus zbiera metryki. Grafana pokazuje wykresy i alerty. Osobny skrypt lub eksporter udostępnia wyniki GitHub Actions jako metryki. | Źródło metryk Edge i eksporter CI. Można wystawić je na Cloud po odebraniu raportów Edge. Dzięki temu Cloud nie potrzebuje nowego połączenia do Edge. Do analizy AI/ML potrzebny jest osobny skrypt, np. z Isolation Forest. |
| **B. Apache + n8n + OpenRouter** | Edge wysyła raport HTTPS do webhooka n8n za Apache. n8n pobiera dane GitHub Actions, liczy wskaźniki i zapisuje wynik. Apache serwuje stronę HTML i plik JSON z danymi. Wybrany model przez OpenRouter klasyfikuje przypadki na podstawie metryk lub podsumowuje alerty. | Uwierzytelnienie webhooka, miejsce na wyniki, prosty dashboard i klucz OpenRouter przechowywany po stronie n8n. Do modelu trafiają tylko statystyki bez tablic. |

Prometheus i Grafana dają gotowe narzędzia do szeregów czasowych i wykresów. Wariant z n8n łatwiej połączyć z webhookiem i API GitHuba, ale trzeba przygotować własną stronę i zapis wyników. Wystarczy wdrożyć **jeden** wariant.

## Jak sprawdzimy, czy analiza pomaga

1. Przygotujemy syntetyczne okna normalnej pracy i oznaczone przypadki anomalii, np. nagły wzrost odmów po nowym wydaniu.
2. Ustalimy regułę bazową, np. ponad 70% odmów w 5 minut przy minimum 20 zdarzeniach.
3. Uruchomimy regułę i wybraną metodę na tym samym zbiorze testowym. Dane testowe odkładamy przed doborem progu, treningiem lub przygotowaniem promptu.
4. Porównamy precision (ile alertów było trafnych), recall (ile anomalii wykryto) i F1. Zapiszemy użyty model i ustawienia.

Decyzję parkingową podejmuje lokalna aplikacja według reguł i abonamentu. Monitoring dostarcza alerty administratorowi.
