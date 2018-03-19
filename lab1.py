import time
from datetime import date
import math

dodaj = 5+3
odejmij = 3-5
mnoz = 5*3
dziel = 5/3
print("dodawanie: ", dodaj, "\nodemnowanie: ", odejmij
, "\nmnozenie: ", mnoz, "\ndzielenie: ", dziel)

print("----------------------------\n")
print ("podaj imie")
imie = input()
print("witaj", imie)

print("----------------------------\n")
print("podaj liczby do zsumowania")
a = input()
b = input()
print("suma wynosi: ", float(a)+float(b))

print("----------------------------\n")
print(sum(range(8,80)))

print("----------------------------\n")
while True:
	print("podaj rok")
	rok = input()
	print("podaj miesiac")
	miesiac = input()
	print("podaj dzien")
	dzien = input()

	przy_data = date(int(rok), int(miesiac), int(dzien))
	akt_data = date.today()
	if przy_data < akt_data:
		print ("podano przeszla date")
		continue
	else:
		odl_czas = abs(przy_data - akt_data)
		print(odl_czas)
		break
	break

print("----------------------------\n")
while True:
	print("Jakie chcesz wykonac dzialanie?\ndodawanie - 1\nodejmowanie - 2\nmnozenie - 3\ndzielenie - 4\nwyjscie - 0")
	dzialanie = input()
	if dzialanie == '0':
		break
	print("podaj liczby")
	a = input()
	b = input()
	if dzialanie == '1':
		print(float(a) + float(b))
	elif dzialanie == '2':
		print(float(a) - float(b))
	elif dzialanie == '3':
		print(float(a) * float(b))
	elif dzialanie == '4':
		print(float(a) / float(b))
	else:
		print("podano nierozpoznane polecenie")
		continue

