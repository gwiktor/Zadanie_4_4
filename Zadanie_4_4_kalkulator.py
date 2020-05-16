import logging
import sys
import math

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

print("Witam w kalkulatorze Wiktora! \n")

#Funkcje poszczególnych działań

def odejmowanie (a,b):
  return a - b

def dzielenie (a,b):
  return a / b

#Funkcja wyboru działania
def wybor_dzialania(dzialanie):
  if dzialanie == 1:
    sys.argv = input("Podaj liczby, które chcesz do siebie dodać rozdzielając każdą spacją. Następnie zatwierdz enterem: ")
    suma = sum(float(arg) for arg in sys.argv if arg.isdigit())
    logging.debug(f"Suma wynosi: {suma}")

  elif dzialanie == 2:
    try:
      while True:
        a = float(input("Podaj składnik 1: "))
        b = float(input("Podaj składnik 2: "))
        logging.debug(f"Odejmuję {b} od {a} \nWynik to {odejmowanie(a, b)}")
        odejmowanie(a, b)
    except ValueError:
      print("Nie wprowadzono liczby")
  
  elif dzialanie == 3:
    sys.argv = input("Podaj liczby, które chcesz ze sobą pomnożyć rozdzielając każdą spacją. Następnie zatwierdz enterem: ")
    iloczyn = math.prod(float(arg) for arg in sys.argv if arg.isdigit())
    logging.debug(f"Iloczyn wynosi: {iloczyn}")

  elif dzialanie == 4:
    try:
      while True:
        a = float(input("Podaj składnik 1: "))
        b = float(input("Podaj składnik 2: "))
        logging.debug(f"Dzielę {a} przez {b} \nWynik to {dzielenie(a, b)}")
        dzielenie(a,b)
    except ValueError:
      print("Nie wprowadzono liczby")
  
  else:
    logging.debug("Wybrałeś niepoprawne działanie")
  
#Wywołanie programu
if __name__ == "__main__":
  dzialanie = int(input("Podaj działanie, posługjąc się odpowiednią liczbą: \n1 - dodawanie \n2 - odejmowanie \n3 - mnożenie \n4 - dzielenie"))
  logging.debug(f"Zostało wywołane działanie numer {dzialanie}")
  wybor_dzialania(dzialanie)

