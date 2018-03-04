annee = input("entrez une annee : ");
annee = int(annee);
print(annee);

if(annee % 4 ) == 0 or (annee % 100) == 0 or (annee % 400) == 0:
    print("c'est une annee bixestile");
elif(annee % 100) != 0 or (annee % 400) != 0 or (annee % 4) != 0:
    print("ce n'est pas une annee bixestile")