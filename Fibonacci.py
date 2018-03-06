import os

def fibonacci(position):
	if(position < 2):
		return position;
	print(((position-1) + (position-2)));

nombre = input("entrez un nombre : ");
nombre = int(nombre);

fibonacci(nombre);
