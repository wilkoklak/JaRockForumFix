# Forum Ja, Rock! FIX!
Ponieważ administracja Ja, Rocka! ma nas, forumowiczów, gdzieś, musimy wziąć
sprawy we własne ręce.

Dlatego powstało to repozytorium.

Dotyczy ono wyglądu forum, a dokładniej tego co można poprawić używając Stylisha.

## Najnowsza wersja
Najnowszą stabilną wersję znajdziesz zawsze w plikach:
* ``main.css``, ``main.min.css`` - dla Chrome, Opery
* ``main_ff.css``, ``main_ff.min.css`` - dla Firefoxa

Pliki ``*.min.css``, to skompresowane wersje kodu - mniej ważą, ale są
praktycznie nieczytelne.

## Co aktualnie jest zmienione?
1. Shoutbox (z mojej starej wersji)
2. Menu (z mojej starej wersji)
3. Wygląd wyszukiwarki
4. Poprawki drobnych niedociągnięć
5. Kolory rang

# Wspomaganie
Każdy użytkownik forum może się przyłączyć. Wystarczą same sugestie zmian, ale
własne edycje są jak najbardziej mile widziane.

Musisz jednak wiedzieć o paru rzeczach...

## Technologie
Używam [Sass](http://sass-lang.com/) do pisania CSS'a. Usprawnia to pracę, a
także ułatwia składanie wszystkich plików w całość.

Nie musisz używać Sass'a, zawsze możesz podesłać pliki w zwykłym CSS'ie a ja je
przerobię na ``*.scss``, aczkolwiek Sass zawsze milej widziany :)
## Struktura
Pliki ``main*.css``, to tylko wynik końcowy. Serce projektu jest w folderze ``css``.

Znajdziesz tam kilka plików, każdy do innej grupy elementów. Musisz znaleźć odpowiedni
dla swoich zmian, lecz jeśli nie znajdziesz, to powinieneś utworzyć plik dla tej kategorii.
## Styl kodu
Zasady:
* twarda tabulatura
* maksymalnie ok. 80 znaków szerokości
* staramy się unikać rozległych zagnieżdżeń
* komentarze, co jest czym, po co, na co, dlaczego tak
* jak najbardziej precyzyjne selektory, aby nie było konfliktów
* wrzucanie zmian do pliku odpowiedniej kategorii

## Skład drużyny
- Artur Boryś (Wilkokłak) - hedmajster projektu ![Kappa](http://how2play.pl/wp-content/uploads/2016/03/Kappa.png)

Chcesz dołączyć do tej listy? Napisz do mnie na forum na PW (Wilkokłak).
