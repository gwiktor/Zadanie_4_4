import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

print("Witam w kalkulatorze Wiktora! \n")

#Funkcje poszczególnych działań
def dodawanie (a):
  wynik = 0
  for skladnik in a:
    wynik += skladnik
  print (f"Wynik dodawania to: {wynik}")

def odejmowanie (a,b):
  return a - b

def mnożenie (a,b):
  return a * b

def dzielenie (a,b):
  return a / b

#Funkcja wyboru działania
def wybor_dzialania(dzialanie):
  if dzialanie == 1:
    logging.info("Podaj liczby, które chcesz do siebie dodać zatwierdzając każdą enterem. Następnie wpisz komendę 'koniec' i zatwierdz enterem")
    try:
      a = []
      while True:
        a.append(float(input()))
    except ValueError:
      logging.debug(f"Wprowadzono następujące liczby: {a}")
      dodawanie(a)
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
    try:
      while True:
        a = float(input("Podaj składnik 1: "))
        b = float(input("Podaj składnik 2: "))
        logging.debug(f"Mnożę {a} razy {b} \nWynik to {mnożenie(a,b)}")
        mnożenie(a, b)
    except ValueError:
      print("Nie wprowadzono liczby")
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

