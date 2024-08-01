#identificación de errores que se pueden cometer y que hacer

#  print(0/0))
"""
line 3
    print(0/0))
              ^
SyntaxError: unmatched ')'
"""

# print(0/0)
"""
line 11, in <module>
    print(0/0)
          ~^~
ZeroDivisionError: division by zero
"""

#print(resultado)

"""
line 19, in <module>
    print(resultado)
          ^^^^^^^^^
NameError: name 'resultado' is not defined
"""

suma=lambda x,y:x+(y*2)
# assert suma(2,2)==4   # la función assert verifica sentencias y si no devuelve error
"""
line 29, in <module>
    assert suma(2,2)==4   # la función assert verifica sentencias y si no devuelve error
           ^^^^^^^^^^^^
AssertionError
"""

edad=10
#if edad<18:
#    raise Exception("no se permiten menores de edad")
#    # esta sentencia es una excepción programada, de aca en adelante el programa no se ejecuta

"""
line 39, in <module>
    raise Exception("no se permiten menores de edad")
Exception: no se permiten menores de edad
"""