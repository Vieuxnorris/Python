
def Fibonacci(position):
    valeur_a = 1;
    valeur_b = 0;
    for i in range(0,position,1):
        valeur_a,valeur_b = valeur_a+valeur_b,valeur_a;
    print valeur_b;

nombre = input("entrez un nombre : ");

Fibonacci(nombre);
