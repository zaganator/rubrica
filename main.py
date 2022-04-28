import os
import re
from classes import Contact


def first_capital(string):
	"""prima lettera della stringa 'upper'"""
	if len(string) < 1:
		return '--'
	return string[0].upper() + string[1:].lower()


def just_letter(string):
	"""return False if there is a digit inside the string"""
	letters = re.compile("\d+")
	return not bool(letters.search(string))


def just_number(string):
	"""return True if there is only number in the string"""
	numbers = re.compile("[a-zA-Z]+")
	return not bool(numbers.search(string))


def create():
	"""return a Contact obj"""
	nome = "1"
	while not just_letter(nome):
		nome = input("nome: ")

	cognome = "1"
	while not just_letter(cognome):
		cognome = input("cognome: ")

	telefono = "a"
	while not just_number(telefono):
		telefono = input("telefono: ")

	return Contact(first_capital(nome), first_capital(cognome), telefono)


# creazione di un loop che crea e aggiunge oggetti ad una lista se giusti
obj_list = []
building_data = True
while building_data:
	a = create()
	a.display()

	# search duplicate in csv file before write on it_______________________
	f = open("rubrica.csv", "r")

	for line in f.readlines():
		lista = line.split(',')
		if a.nome == lista[0] and a.cognome == lista[1]:
			print(f"trovato un contatto simile >> {line}")
		if a.telefono in lista[2]:
			print(f"il numero sembra essere uguale >> {line}")

	f.close()
	# ______________________________________________________________________

	# conditions to save data_______________________________________________
	if input("inserimento corretto? S/N ").lower() != 'n':
		obj_list.append(a)
	if input("continuare? S/N ").lower() == 'n':
		print("Closing script...")
		building_data = False
	# ______________________________________________________________________

		# data saving in a csv file_________________________________________
		f = open("rubrica.csv", "a")
		print("...saving data...")
		for item in obj_list:
			csv_contact = item.obj_to_csv()
			f.write(csv_contact)
		f.close()
		print("Data Saved.")
		# __________________________________________________________________

