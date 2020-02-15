import sys

wygrana = 0

def wstep():
    print("Witaj w grze Milionerzy, przed Tobą 15 pytań do miliona")
    imie = input("Podaj imię: ")
    print("Twoje obecne saldo to:", wygrana, " zł", imie, "- Zaczynamy grę")
    pytania()

def pytania():
    pytanie("Pytanie na rozgrzewkę. \n", "Jaka jest stolica Polski? \n", "A. Warszawa", "B. Berlin", "C. Paryż", "D. Krakow", 500, 0, "A. Warszawa", wygrana)
    pytanie("Dobrze, Nastepne pytanie!. \n", "Kto jest prezydentem USA? \n", "A. Jaroslaw", "B. Lepper", "C. Walęsa", "D. Trump", 1000, 500, "D. Trump", wygrana)
    pytanie("Coraz lepiej!. Ale przed nami jeszcze dużo pytań. Oto następne:  \n", "Jaki jest wzór na pole kwadratu? \n", "A. a x b", "B. b2 - 4ac", "C. (a x b) + c2", "D. a x a", 2000, 1000,  "D. a x a", wygrana)
    pytanie("Trzy poprawne odpowiedzi! Czas skończyć z prostymi pytaniami! A więc do rzeczy. \n", "Jaki jest skrót dla Structured Query Language? \n", "A. ABC", "B. C#", "C. SQL", "D. JAVA", 5000, 2000, "C. SQL", wygrana)
    pytanie("Dobrze! \n", "W takim razie co ty an to? Rozwiń skrót HTTP: \n", "A. Hiper Jezyk", "B. Hypertext Transfer Protocol", "C. Hej Ty P", "D. Jakas odp", 10000, 5000, "B. Hypertext Transfer Protocol", wygrana)
    pytanie("Nieźle, lecisz jak burza! Jedziemy dalej.  \n", "Organizator naszego kursu i dzisiejszego Hackatonu - CODE:ME, to: \n", "A. hospicjum", "B. obóz koncentracyjny", "C. fundacja", "D. restauracja", 20000, 10000, "C. fundacja", wygrana)
    pytanie("Połowa pytań już za tobą! \n", "GIT to: \n", "A. Rozproszony system kontroli wersji", "B. System Operacyjny", "C. Nazwa piekarni", "D. Miasto w Holandii", 40000, 20000, "A. Rozproszony system kontroli wersji", wygrana)
    pytanie("Swietnie! \n", "W takim razie, kto jest twórcą wspomnianego GITa? \n" "A. Jan Paweł II", "B. Donald Trump","C. Linus Torvalds", "D. Aleksander Kwaśniewski", "C. Linus Torvalds", 75000, 40000, "C. Linus Torvalds", wygrana)
    pytanie("Kolejna dobra odpowiedz! \n", "Jakim typem zmiennej określamy liczbe zmiennoprzecinkową w Pythonie:\n", "A. boolean", "B. string", "C. integer", "D. float", 125000, 75000, "D. float", wygrana)
    pytanie("Bardzo dobrze! \n", "Jaki operator w Pythonie służy do określenia [jest różne]? \n", "A. //", "B. +=", "C. !=", "D. ==", 250000, 125000, "C. !=", wygrana)
    pytanie("Dobrze! Widać, że słuchałeś na zajęciach! \n", "Jaki polski celebryta jest młodszy z każdym mijającym rokiem? \n", "A. Janusz Korwin Mikke", "B. Krzysztof Ibisz", "C. Lech Wałęsa", "D. Doda", 500000, 250000, "B. Krzysztof Ibisz", wygrana)
    pytanie("Dokładnie, Krzysiu Ibisz wiecznie młody a my dotarliśmy do ostatniego pytania!!! \n", "CI/CD jest: \n", "A. Częścią metodyki DevOps", "B. Zespołem Rockowym", "C. Losowymi literkami", "D. Rodzajem płyt CD", 1000000, 500000, "A. Częścią metodyki DevOps", wygrana)
    print("Gratulacje wygrałeś milion")
    exit


def pytanie(pocieszenie, tresc_pytania, odpowiedz_1, Odpowiedz_2, odpowiedz_3, odpowiedz_4, kwota_pytania, poprzednia_kwota, poprawna_odpowiedz, wygrana):
    # odpowiedz = input(tresc_pytania) # poniższe linie można zastąpić jedną
    print(tresc_pytania)
    print(odpowiedz_1, Odpowiedz_2, odpowiedz_3, odpowiedz_4)
    co_dalej = input("Czy chcesz grać dalej (Tak/Nie)\n")
    if co_dalej == "Nie":
        print("Gratulacje, wygrałeś: ", poprzednia_kwota)
        sys.exit()

    else:
        kolo = input(print("Czy potrzebujesz kół ratunkowych:(Tak/Nie):"))
        if kolo == "Tak":
            wybor = input("50/50 wybierz ""1"", Pytanie do publicznosci wybierz ""2")
            if wybor == "1":
                lista1 = [odpowiedz_1, Odpowiedz_2, odpowiedz_3, odpowiedz_4]
                lista1.remove(str(poprawna_odpowiedz))
                import random
                print(str(random.sample(lista1, 1)) + str(poprawna_odpowiedz))
                odpowiedz = input("Podaj odpowiedz:")
            else:
                print("publiczność mówi że:", poprawna_odpowiedz)
                odpowiedz = input("Podaj odpowiedz:")
                if odpowiedz == poprawna_odpowiedz:
                    print("Brawo, to jest poprawna odpowiedź")
                    wygrana = kwota_pytania
                    print("Twoje saldo to:", wygrana, " zł")
                else:
                    print("Niestety to jest błędna odpowiedż, poprawna odpowiedź to:", poprawna_odpowiedz, "koniec gry")
                    wygrana = 0
                    wstep()
        else:
            print(tresc_pytania)
            odpowiedz = input("Podaj odpowiedz:")
            if odpowiedz == poprawna_odpowiedz:
                print("Brawo, to jest poprawna odpowiedź")
                wygrana = kwota_pytania
                print("Twoje saldo to:", wygrana, " zł")
            else:
                print("Niestety to jest błędna odpowiedż, poprawna odpowiedź to:", poprawna_odpowiedz, "koniec gry")
                wygrana = 0
                wstep()

wstep()
