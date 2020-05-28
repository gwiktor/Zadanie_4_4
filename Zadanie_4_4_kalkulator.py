import logging
import sys
import math

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

print("Witam w kalkulatorze Wiktora! \n")

#Funkcje poszczególnych działań

def dodawanie (*args):
  suma = sum(args)
  logging.debug(f"Suma liczb wynosi: {suma}")
  return suma

def odejmowanie (a,b):
  logging.debug(f"Różnica liczb wynosi: {a - b}")
  return a - b

def dzielenie (a,b):
  logging.debug(f"Dzielenie liczb wynosi: {a / b}")
  return a / b

def mnożenie (*args):
  iloczyn = math.prod(args)
  logging.debug(f"Iloczyn liczb wynosi: {iloczyn}")
  return iloczyn

#Zdefiniowanie wywołań
dzialania = {
  1: dodawanie,
  2: odejmowanie,
  3: mnożenie,
  4: dzielenie
}

#Funkcja wyboru działania
def wybor_dzialania(dzialanie):
  if dzialanie == 1 or dzialanie == 3:
    args = list(map(int, input("Wprowadz liczby oddzielając spacją: ").split()))
  elif dzialanie == 2 or dzialanie == 4:
    a = int(input("Podaj pierwszy składnik: "))
    b = int(input("Podaj drugi składnik: "))
    args = (a, b)
  else:
    logging.debug("Wybrałeś niepoprawne działanie")
    return
  wynik = dzialania[dzialanie](*args)
  return wynik

#Wywołanie programu
if __name__ == "__main__":
  while True:
    dzialanie = int(input("Podaj działanie, posługjąc się odpowiednią liczbą: \n1 - dodawanie \n2 - odejmowanie \n3 - mnożenie \n4 - dzielenie"))
    logging.debug(f"Zostało wywołane działanie numer {dzialanie}")
    wybor_dzialania(dzialanie)