def suma(a, b):
    """
    Retorna la suma de dos números.

    Ejemplo:
    >>> suma(2, 3)
    5
    >>> suma(-1, 1)
    0
    >>> suma(0,'a')
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()