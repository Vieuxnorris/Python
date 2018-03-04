import string
import os

joueur = input("nombre de chiffre : ");
joueur = int(joueur);

nombre = [];
i=0;

for i in range(joueur):
        choix = input("entrez un nombre : ");
        choix = int(choix);
        nombre.append(choix);
        print(nombre);

verification = input("tu veux inverser la liste 0->x(tape 'P') ou x->0(tape 'p') : ");
verification = str(verification);
while verification.lower() != 'p':
        print("erreur");
        verification = input("entrez 'P' ou 'p' svp : ");

if verification == 'p':
        nombre.sort();
        print(nombre);
elif verification == 'P' :
        nombre.sort(reverse=True);
        print(nombre);

os.system("pause");
