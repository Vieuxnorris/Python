def table_de_multiplication(nombre,multiplicateur):
    for i in range(1,multiplicateur+1,1):
        print(nombre," * ",i, " = ", nombre*i);


nombre = input("entrez un nombre : ");
multiplicateur = input("entre le multiplicateur : ");
nombre = int(nombre);
multiplicateur = int(multiplicateur);
table_de_multiplication(nombre,multiplicateur);