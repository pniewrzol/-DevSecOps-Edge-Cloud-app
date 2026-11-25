# M2 – Co może pójść źle (STRIDE)

STRIDE to sześć grup zagrożeń. Sprawdzamy, co może się stać przy API, lokalnej bazie, przesyłaniu raportu i publikacji obrazu. Chronimy poprawność decyzji, dane w SQLite, dostępność usługi, klucze oraz obraz wdrożeniowy.

| Grupa | Przykład w SmartGate | Ochrona | Jak to sprawdzimy |
|---|---|---|---|
| **S** – podszywanie się | Obcy klient udaje klienta Edge lub wysyła fałszywy raport do Cloud. | API wymaga klucza. Odbiornik raportów ma mieć osobny klucz i HTTPS. | Test braku lub złego klucza już przechodzi. Test odbiornika jest w planie. |
| **T** – zmiana danych | Ktoś podmienia abonament w SQLite, raport albo obraz. | Ograniczyć prawa do bazy, identyfikować raporty i wdrażać sprawdzony obraz po digescie. | Sprawdzić uprawnienia pliku, ponowienie raportu i zgodność digestu. |
| **R** – brak dowodu operacji | Po awarii trudno ustalić, która wersja działała i kto uruchomił wdrożenie. | Zapisywać identyfikator przebiegu, digest, czas i wynik wdrożenia. | Powiązać log wdrożenia i rollbacku z przebiegiem CI. |
| **I** – ujawnienie danych | Klucz API albo numer tablicy trafia do logów lub monitoringu. | Dane testowe są fikcyjne. API podsumowania zwraca liczniki. Klucze mają być poza repozytorium i logami. | Test podsumowania sprawdza brak tablicy. Przejrzeć logi przed pokazem. |
| **D** – brak dostępności | Cloud przestaje odpowiadać albo nowa wersja Edge nie startuje. | Edge korzysta z lokalnej bazy. W planie są ponowienia raportów, healthcheck i rollback. | Odłączyć Cloud w laboratorium i potwierdzić lokalną decyzję. Sprawdzić powrót do działającego obrazu. |
| **E** – zbyt duże uprawnienia | Zadanie testowe dostaje prawo zapisu do rejestru albo Cloud może inicjować połączenia do Edge. | Publikacja ma osobne uprawnienie zapisu. CHR ma dopuszczać tylko wymagany ruch między VM. | Przejrzeć uprawnienia workflow i sprawdzić dozwolone oraz zablokowane połączenia. |

**Osobna próba CI:** w kontrolowanym teście potwierdzić, że wynik `CRITICAL` zatrzymuje publikację. W M2 potwierdziliśmy udany przebieg, a scenariusz blokady jest w [backlogu](06-backlog.md).
