
def Fibonacci_helper(position):
    position -= 1;
    return (position + (position-1));


def Fibonacci(position):
    if(position <= 2):
        print(position);
    else:
        print(Fibonacci_helper(position));


nombre = input("entrez un nombre : ");
nombre = int(nombre);

Fibonacci(nombre);
