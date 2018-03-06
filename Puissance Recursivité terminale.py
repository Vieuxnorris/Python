
def power(a,b):
    if(b < 1):
        return 1
    else:
        result = a * power(a,b-1);
        return result;

a = input("entrez votre nombre : ");
b = input("entrez votre nombre : ");

print(power(a,b));
