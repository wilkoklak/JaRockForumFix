# Forum Ja, Rock! FIX!
Ponieważ administracja Ja, Rocka! ma nas, forumowiczów, gdzieś, musimy wziąć
sprawy we własne ręce.

Dlatego powstało to repozytorium.

Dotyczy ono wyglądu forum, a dokładniej tego co można poprawić używając Stylisha.
## Założenia
Każdy forumowicz, który zna się na CSS'ie, może dodać coś od siebie. Ulepszamy
rózne rzeczy - od shoutboxa, przez menu i tagi, po kolorystykę i typografię.

Osoby, które nie mają pojęcia o CSS'ie mogą zgłaszać propozycje elementów do poprawy,
a jeżeli chcą się nauczyć, to polecam http://w3schools.com/css

**WAŻNE!** Nie wszystko można osiągnąć używając samego CSS'a. Służy on wyłącznie
do edycji wyglądu elementów, ewentualnie animacji (CSS3). Nie możemy nim zmieniać
treści elementów, ich zachowania (tylko wizualnie, np. zmiana koloru po najechaniu) itd.
## Struktura
W folderze CSS można znaleźć plik ze stylem dla grupy elementów, np. shoutbox, menu.
Ma to na celu ułatwienie edycji - przy zbyt dużych plikach łatwo można się zgubić.

Jeśli nie możesz znaleźć odpowiedniego pliku dla Twojej edycji, to utwórz go sam.
Nie przejmuj się jeśli się pomylisz w nazewnictwie - przed wdrożeniem każda edycja
jest weryfikowana przez odpowiednie osoby i zostaniesz powiadomiony o ewentualnej
konieczności poprawy.

Pliki te potem są łączone do jednego pliku. W zasadzie jest mowa o dwóch plikach, jeden dla Chrome i Opery (main.css), a drugi
dla Firefoxa (potrzebne są dodatkowe nagłówki, main_ff.css).

Następnie pliki te są minimalizowane (minify, uglify, zwał jak zwał), aby były mniejsze.
Są to pliki \*.min.css

## Styl kodu
Osobiście do edycji używam [Atoma](http://atom.io), ale możesz używać innego edytora.
Ważne jest natomiast, żeby tabulatura była "twarda", czyli nie składała się ze spacji,
a po prostu była osobnym znakiem - to pozwoli na zachowanie jednakowego wyglądu we wszystkich
edytorach i we wszystkich fragmentach kodu.

Staraj się ograniczać szerokość linijki do 80 znaków!
Niektóre edytory (np. Atom, Notepad++) mogą wyświetlać kreskę, która sugeruje, że należy przejść
do następnej linijki.

Ważne jest także dodawanie komentarzy do możliwie jak największej ilości selektorów
i atrybutów - to ułatwi pracę innym, a także Tobie kiedy zajrzysz do kodu po dłuższej
przerwie.

Korzystamy ze wszelkich udogodnień CSS3 (Kill Internet Explo(it)rer!!! NO REMRoSE!!11!!1)

Przykład (w markdownie tabulatory są zastępowane spacjami):

```css
/* Wygląd rozwijalnego elementu menu */
#more_apps_menucontent {
	box-shadow: unset; /* usunięcie cieni */
	background: #d10915; /* zmiana koloru tła */
}
```
## Co aktualnie jest zmienione?
1. Shoutbox (z mojej starej wersji)
2. Menu (z mojej starej wersji)

## Skład drużyny
- Artur Boryś (Wilkokłak) - hedmajster projektu ![Kappa](http://how2play.pl/wp-content/uploads/2016/03/Kappa.png)

Chcesz dołączyć do tej listy? Napisz do mnie na forum na PW (Wilkokłak).
