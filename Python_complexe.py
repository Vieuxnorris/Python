import string
import os

def convertion(nombre):
    nombre = str(nombre);
    nombre_entier,nombre_flottant = nombre.split(".");
    nombre = ",".join([nombre_entier,nombre_flottant[:3]]);
    print(nombre);

nombre = input("entrez un nombre float : ");

convertion(nombre);
