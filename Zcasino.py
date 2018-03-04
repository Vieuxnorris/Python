import math;
import random;

def roulette(nombre_de_jetons,somme):
        nombre_aleatoire = random.randrange(50);
        print("la roulette a comme valeur : ",nombre_aleatoire);
        if(nombre_de_jetons == nombre_aleatoire):
            print("vous avez win ! voici votre argent : ", somme*3);
        elif(nombre_de_jetons != nombre_aleatoire):
            if(nombre_aleatoire % 2) == (nombre_de_jetons % 2):
                print("vous avez la même couleur : ", somme/2);
            else:
                print("vous avez perdu dommage");






verification = False;
while verification == False:
    nombre_de_jetons = input("donner un nombre entre 0 à 49 : ");
    nombre_de_jetons = int(nombre_de_jetons);
    if(nombre_de_jetons < 0 or nombre_de_jetons > 49):
        verification = False;
    else:
        verification = True;
somme = input("combien voulez-vous mettre : ");
somme = int(somme);
roulette(nombre_de_jetons,somme);

