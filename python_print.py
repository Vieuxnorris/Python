import string

def test(*par,sep=" ", espace="\n"):
    for i,valeur in enumerate(par):
        par = str(valeur);
    chaine = par.split(sep);
    chaine = espace.join(chaine);
    verification = input("entrez 'M' pour majuscule ou 'm' pour minuscule : ");
    verification = str(verification);
    while verification.lower() != 'm':
        print("erreur");
        verification = input("entrez la lettre 'M' ou 'm' : ");

    if verification == 'M' :
        chaine = chaine.upper();
        print(chaine);
    elif verification == 'm':
        chaine = chaine.lower();
        print(chaine);

chaine = input("entrez une phrase : ");

test(chaine);