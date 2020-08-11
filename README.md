# ForgeOfEmpire
Program do obsługi gry przeglądarkowej Forge of Empire. Jego zadaniem jest w głównej mierze zbieranie zakończonych zbiorów oraz załączanie nowej produkcji. Działanie programu oparte jest w głównej mierze na bibliotece pyautogui (kontrola ruchów myszki, screenshoty, znajdowanie elementów graficznych na  ekranie).


Krótki opis plików:
- manage.py
W pliku zdefiniowane zostały funkcję, które:
  - załączają produkcję
  - dokonują zbiorów zakończonej produkcji
  - klikają przycisk wsparcie przyjaciół
  - zwalniają tawernę
Funkcje działają w oparciu o bibliotekę pyautogui rozpoznając budynki, identyfikując obszary z dostępnymi "zbiorami".
  
- login.py
Przy użyciu biblioteki Selenium program otwiera przeglądarkę oraz loguje się na konto.

- play.py
Program przewija obraz wyświetlany na ekranie aby otrzymać dostęp do odpowiednich obszarów gry oraz wykorzystując funkcje zdefiniowane
w manage.py wykonując określone zadania.
