import logging

#Tworzenie logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")

print("Witam w kalkulatorze Wiktora! \n")

def dodawanie (a,b):
  #Funkcja dodawania
  return a + b

def odejmowanie (a,b):
  #Funkcja odejmowania
  return a - b

def mnożenie (a,b):
  #Funkcja mnożenia
  return a * b

def dzielenie (a,b):
  #Funkcja dzielenia
  return a / b


dzialanie = int(input("Podaj działanie, posługjąc się odpowiednią liczbą: \n1 - dodawanie \n2 - odejmowanie \n3 - mnożenie \n4 - dzielenie"))
a = float(input("Podaj składnik 1: "))
b = float(input("Podaj składnik 2: "))


if dzialanie == 1:
  logging.info("Dodaję", a, "i", b, "\nWynik to ", dodawanie(a, b))
  dodawanie(a,b)
  
elif dzialanie == 2:
  logging.info("Odejmuję", b, "od", a, "\nWynik to", odejmowanie(a, b))
  odejmowanie(a, b)

elif dzialanie == 3:
  logging.info("Mnożę", a, "razy", b, "\nWynik to", mnożenie(a,b))
  mnożenie(a, b)
  
elif dzialanie == 4:
  logging.info("Dzielę", a, "przez", b, "\nWynik to", dzielenie(a, b))
  dzielenie(a,b)
  
else:
  logging.info("Wybrałeś niepoprawne działanie")
