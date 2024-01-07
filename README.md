# Projekt Battleships

![Menu Start](images/menu.png)

- [Projekt Battleships](#projekt-battleships)
  - [Dokumentacja w Kodzie](#dokumentacja-w-kodzie)
  - [Dane autora](#dane-autora)
  - [Cel i Opis Projektu](#cel-i-opis-projektu)
    - [Cel Projektu](#cel-projektu)
    - [Opis Projektu](#opis-projektu)
      - [Instrukcja Gracza](#instrukcja-gracza)
      - [Funkcje Komputera](#funkcje-komputera)
  - [Podział Programu na Klasy i Opis Klas](#podział-programu-na-klasy-i-opis-klas)
  - [Instrukcja Użytkownika](#instrukcja-użytkownika)
    - [Wykorzytane moduły](#wykorzytane-moduły)
    - [Instalacja niebędnych modułów](#instalacja-niebędnych-modułów)
    - [Uruchomienie gry w trybie developera](#uruchomienie-gry-w-trybie-developera)
    - [Opis Formatu Plików Konfiguracyjnych](#opis-formatu-plików-konfiguracyjnych)
    - [Testy](#testy)
  - [Wymagania sprzętowe](#wymagania-sprzętowe)
  - [Część Refleksyjna](#część-refleksyjna)
  - [Zakończenie](#zakończenie)

## Dokumentacja w Kodzie

Dokumentacja w kodzie jest realizowana poprzez tzw. docstrings.

## Dane autora

**Autor:** Łukasz Szydlik
**Email:** <01187295@pw.edu.pl>

## Cel i Opis Projektu

### Cel Projektu

Celem projektu jest stworzenie interaktywnej gry w statki, która umożliwi graczowi rywalizację z komputerem. Komputer ma za zadanie wykonywać logiczne ruchy, zgodne z zasadami gry w statki.

### Opis Projektu

Gra w statki to klasyczna gra strategiczna, w której dwaj gracze umieszczają swoje statki na planszy i starają się zatopić statki przeciwnika, oddając strzały na przemian. W naszym projekcie gracz będzie miał możliwość rywalizacji z komputerem, który będzie sterował własnymi statkami.

#### Instrukcja Gracza

1. **Rozstawienie statków:**
   - Gracz rozstawia swoją flotę na planszy poprzez wybranie i umieszczenie statku za pomocą lewego przyciskiu myszy. Po wybraniu statku, gracz ma możliwość **obrócenia** okrętu klikając prawy przycisk myszy.
   - Gracz może wybrać również losowe rostawienie za pomoą przycisku **Randomize**
   - Wciśnięcie przycisku **Reset** spowoduje powrót statków na domyślną pozycję
  
2. **Rozpoczęcie rozgrywki:**
   - Po rozstawieniu statków gracz klika przycisk **Deploy**, by rozpocząć rozgrywkę

3. **Oddanie strzału:**
   - W celu oddania strzału, gracz klika pozycję na planszy komputera i zatwierdza ją lewym przyciskiem myszy

4. **Przyciski Menu i Quit**
   - Przycisk **Menu**: Cofnięcie się do menu startowego
   - Przycisk **Quit**: Wyjście z gry

#### Funkcje Komputera

1. **Logiczne Ruchy:**
   - Komputer wykonuje logiczne ruchy, starając się trafiać w statki przeciwnika.
  
2. **Sprawdzanie Poprawności Strzałów:**
   - Komputer nie strzela w pola, w których na pewno nie może być statku

3. **Odkrywanie Reszty Statku:**
   - Po trafieniu komputer stara się odkryć resztę statku, strzelając w pionie lub poziomie.

![Menu Start](images/game.png)

## Podział Programu na Klasy i Opis Klas

Projekt został podzielony na następujące klasy:

1. **Klasa 1:**
   - Krótki opis klasy 1.

2. **Klasa 2:**
   - Krótki opis klasy 2.

## Instrukcja Użytkownika

W celu uruchomienia gry należy uruchomić terminal i przejść do folderu z plikiem main.py

Następnie wpisać komendę:

```python
python3 main.py
```

---

### Wykorzytane moduły

W projekcie zostały wykorzystane następujące moduły:

- standardowe
  - typing
  - random
  - argparse
  - math
  - pytest
- niestandardowe
  - NumPy
  - PyGame

---

### Instalacja niebędnych modułów

W celu zainstalowania niezbędnych modułów należy użyć komendy:

```python
python3 -m pip install -r requirements.txt
```

---

### Uruchomienie gry w trybie developera

Grę można uruchomić w trybie developera poprzez:

```python
python3 main.py -d
```

Umożliwi to użytkownikowi dostep do wyświetlenia aktulanej logiki plansz gry w terminalu poprzez wciśniśnięcie środkowego przycisku myszy.

---

### Opis Formatu Plików Konfiguracyjnych

W projekcie występuje plik konfiguracyjny: **screen_resolution.txt**

W tym pliku użytkownik może wpisać rozmiary ekranu gry (podane w pikselach) zgodnie z następującym formatem domyślnym:

```txt
screen_width=1280
screen_height=720
```

W razie jakichkolwiek błedów rozmiar ekranu po uruchomienu programu ustawi się na wartości domyślne. Następnie proszę ponownie uruchomić grę.

---

### Testy

Domyślne testy sprawdzjące logikę planszy gry oraz wyjątków związanych z plikiem konfiguracyjnym znajdują się w pliku test_battleships.py i działają poprzez framework pytest.

## Wymagania sprzętowe

Zainstalowany: [Python3](https://www.python.org/downloads/)  
Minimalna rozdzielczość: 800x600

## Część Refleksyjna

- Co udało się osiągnąć:
  - Stworzono w pełni działającą grę statki z interfejsem graficznym.
- Rzeczy, które nie zostały zrealizowane, z komentarzem dlaczego.
  - Nie dopracoano funckji load_image() znajdującej się w pliku settings.py która przez implementację w złym miejscu już podczas importowania settings.py inicjalizuje ekran gry. Zabrakło czasu na refaktoryzcję kodu poprzez umieszcznie funckji i zładowanie wszytkich grafik w main.py
- Przeszkody napotkane podczas projektu i jak zostały one przezwyciężone.
  - Funkcja która ma na celu dopasowanie statku do planszy, gdy jego fragment w momencie ustawiania wystawał poza planszę nie została idealnie dopracowana. Nie udało się rozwiązać dopasowania do planszy w przypadku, gdy statek jest w większości poza planszą, a dotyka jedynie rogu planszy, gdyż statek ustawiał się w taki sposób, że wystwał poza planszę. W tej sytuacji zdecydowałem się, że w takim przypadku statek powróci na swoją domyślną pozycję i będzie możliwy do ponownego ustawienia.
- Zmiany w stosunku do pierwotnego planu rozwiązania.
  - Pierwtotnie statki miały być rozstawiane bez możliwości sąsiadowania ze sobą. Jednakże przez ograniczoną ilość czasu zrezygnowałem z tej opcji.

## Zakończenie

Dziękuję za uwagę i zapraszam do korzystania z gry!
