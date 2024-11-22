def suma_ (a,b):
    return a+b
def resta_ (a,b):
    return a-b
def mult_ (a,b):
    return a*b
def div_ (a,b):
    if b==0:
        raise ValueError("no se puede dividir entre 0")
    return a/b

if __name__ == "__main__":

    # este archivo al tener el if __name__ se puede llamar y se va a ejecutar el código de aca en adelante, 
    # supongamos que este archivo es una librería de otro archivo, lo que hace el if __name__ es que no ejecute todo sino lo que esta arriba del if __name__


    print ('operaciones')

    sumas_ = suma_ (2,3)
    print(f'suma: {sumas_}')