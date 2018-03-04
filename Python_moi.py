import string;

chaine = input("entrez votre phrase : ");
chaine = str(chaine);
validation = input("m pour minuscule, M pour majuscule : ");
validation = str(validation);

while validation.lower() != "m":
    print("m ou M svp : ");
    validation = input();

i=0;

for i in range(0,len(chaine),1):
    if(validation == "M"):
        chaine = chaine.upper();
        print(chaine[i]);
    elif(validation == "m"):
        chaine = chaine.lower();
        print(chaine[i]);


ma_liste = list(chaine);
print(ma_liste);
